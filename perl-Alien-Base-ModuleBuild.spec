#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Alien
%define		pnam	Base-ModuleBuild
Summary:	Alien::Base::ModuleBuild - Module::Build subclass for building Alien:: modules and their libraries
Summary(pl.UTF-8):	Alien::Base::ModuleBuild - podklasa Module::Build do budowania modułów Alien:: oraz ich bibliotek
Name:		perl-Alien-Base-ModuleBuild
Version:	1.14
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d9480f0c8891428950eb35536026ded0
URL:		https://metacpan.org/release/Alien-Base-ModuleBuild
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Shell-Config-Generate
BuildRequires:	perl-Shell-Guess
BuildRequires:	perl-Alien-Base >= 1.20
BuildRequires:	perl-Capture-Tiny >= 0.17
BuildRequires:	perl-File-chdir >= 0.1005
BuildRequires:	perl-Path-Tiny >= 0.077
BuildRequires:	perl-Sort-Versions
BuildRequires:	perl-URI
BuildRequires:	perl-Test2-Suite >= 0.000060
%endif
Requires:	perl-Alien-Base >= 1.20
Requires:	perl-File-chdir >= 0.1005
Requires:	perl-Path-Tiny >= 0.077
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a subclass of Module::Build, that with Alien::Base allows for
easy creation of Alien distributions. This module is used during the
build step of your distribution. When properly configured it will:
- use pkg-config to find and use the system version of the library
- download, build and install the library if the system does not
  provide it.

NOTE: Please consider for new development of Aliens that you use
Alien::Build and alienfile instead. Like this module they work with
Alien::Base. Unlike this module they are more easily customized and
handle a number of corner cases better.

%description -l pl.UTF-8
Ten pakiet zawiera podklasę Module::Build, która w połączeniu z
Alien::Base pozwala na łatwe tworzenie pakietów Aliena. Ten moduł jest
używany podczas kroku budowania pakietu. Przy poprawnym
skonfigurowaniu:
- użyje pkg-configa do znalezienia i używania systemowej wersji
  biblioteki
- pobierze, zbuduje i zainstaluje bibliotekę, jeśli system jej nie
  dostarcza.

UWAGA: do tworzenia nowych Alienów należy rozważyć użycie Alien::Build
i alienfile zamiast tego pakietu. Podobnie jak ten moduł działają z
Alien::Base, ale można je łatwiej dostosować i lepiej obsługują wiele
przypadków brzegowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Alien/Base/ModuleBuild/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Alien/Base/ModuleBuild.pm
%{perl_vendorlib}/Alien/Base/ModuleBuild
%{_mandir}/man3/Alien::Base::ModuleBuild*.3pm*
