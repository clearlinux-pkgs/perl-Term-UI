#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Term-UI
Version  : 0.46
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Term-UI-0.46.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Term-UI-0.46.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libterm-ui-perl/libterm-ui-perl_0.46-1.debian.tar.xz
Summary  : 'User interfaces via Term::ReadLine made easy'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Term-UI-license = %{version}-%{release}
Requires: perl-Term-UI-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Log::Message)
BuildRequires : perl(Log::Message::Simple)

%description
Please refer to 'perldoc Term::UI' after installation for details.
#####################################################################

%package dev
Summary: dev components for the perl-Term-UI package.
Group: Development
Provides: perl-Term-UI-devel = %{version}-%{release}
Requires: perl-Term-UI = %{version}-%{release}

%description dev
dev components for the perl-Term-UI package.


%package license
Summary: license components for the perl-Term-UI package.
Group: Default

%description license
license components for the perl-Term-UI package.


%package perl
Summary: perl components for the perl-Term-UI package.
Group: Default
Requires: perl-Term-UI = %{version}-%{release}

%description perl
perl components for the perl-Term-UI package.


%prep
%setup -q -n Term-UI-0.46
cd %{_builddir}
tar xf %{_sourcedir}/libterm-ui-perl_0.46-1.debian.tar.xz
cd %{_builddir}/Term-UI-0.46
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Term-UI-0.46/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Term-UI
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Term-UI/7ef1cc1be0863727457d04623ccac33e2edf9a84
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Term::UI.3
/usr/share/man/man3/Term::UI::History.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Term-UI/7ef1cc1be0863727457d04623ccac33e2edf9a84

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Term/UI.pm
/usr/lib/perl5/vendor_perl/5.30.3/Term/UI/History.pm
