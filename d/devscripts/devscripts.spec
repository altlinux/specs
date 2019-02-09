Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-build-python3 rpm-macros-fedora-compat
BuildRequires: perl(Authen/SASL.pm) perl(Date/Format.pm) perl(Date/Parse.pm) perl(File/Which.pm) perl(GitLab/API/v4/Constants.pm) perl(HTTP/Date.pm) perl(HTTP/Headers.pm) perl(HTTP/Status.pm) perl(IO/Uncompress/AnyUncompress.pm) perl(JSON.pm) perl(LWP/Protocol/https.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Net/SMTPS.pm) perl(Pod/Usage.pm) perl(SOAP/Lite.pm) perl(String/ShellQuote.pm) perl(Term/ANSIColor.pm) perl(Term/Size.pm) perl(Try/Tiny.pm) perl(YAML/Syck.pm)
# END SourceDeps(oneline)
# we do not have them
%filter_from_requires /^python3.apt/d
%filter_from_requires /^python3.debian.changelog/d
%filter_from_requires /^python3.debian.deb822/d
%filter_from_requires /^python3.debian./d

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           devscripts
Version:        2.19.2
Release:        alt1_1
Summary:        Scripts for Debian Package maintainers

License:        GPLv2+
URL:            https://packages.debian.org/sid/%{name}
Source0:        http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
# Fixes path to xsl-stylesheet manpages docbook.xsl
Patch0:         devscripts_docbook.patch
# Removes the debian-only --install-layout python-setuptools option
Patch1:         devscripts_install-layout.patch
# Install some additional man pages
Patch2:         devscripts_install-man.patch

BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(DB_File.pm)
BuildRequires:  perl(Digest/MD5.pm)
BuildRequires:  perl(Dpkg/Changelog/Debian.pm)
BuildRequires:  perl(Dpkg/Changelog/Parse.pm)
BuildRequires:  perl(Dpkg/Control.pm)
BuildRequires:  perl(Dpkg/Control/Hash.pm)
BuildRequires:  perl(Dpkg/Vendor.pm)
BuildRequires:  perl(Dpkg/Version.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Encode/Locale.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(feature.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(File/DesktopEntry.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/HomeDir.pm)
BuildRequires:  perl(FileHandle.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(filetest.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(Git/Wrapper.pm)
BuildRequires:  perl(IO/Dir.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IPC/Run.pm)
BuildRequires:  perl(JSON/PP.pm)
BuildRequires:  perl(List/Compare.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
BuildRequires:  perl(Net/SMTP.pm)
BuildRequires:  perl(open.pm)
BuildRequires:  perl(Parse/DebControl.pm)
BuildRequires:  perl(Pod/Checker.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Text/ParseWords.pm)
BuildRequires:  perl(Text/Wrap.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(URI/QueryParam.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)

BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt xsltproc
BuildRequires:  po4a
BuildRequires:  python3-devel
BuildRequires:  python3-module-distribute
BuildRequires:  /usr/bin/dpkg-buildflags
BuildRequires:  /usr/bin/dpkg-vendor
BuildRequires:  /usr/bin/dpkg-parsechangelog
BuildRequires:  /usr/bin/help2man

Requires:       dpkg
# man for manpage-alert
Requires:       %{_bindir}/man

Requires:       checkbashisms
Source44: import.info


%description
Scripts to make the life of a Debian Package maintainer easier.

%package -n python3-module-%name
Group: Development/Python3
Summary: Python bingings for %name
Buildarch: noarch
%description -n python3-module-%name
Python bingings for %name, %summary


%package -n checkbashisms
Group: Development/Other
Summary:        Devscripts checkbashisms script

%description -n checkbashisms
This package contains the devscripts checkbashisms script.


%package compat
Group: Development/Other
Summary:        Compatibility package for devscripts-minimal
Requires:       perl-App-Licensecheck
Requires:       checkbashisms = %{version}-%{release}
Obsoletes:      devscripts-minimal < 2.16.6-1

%description compat
This package only exists to help transition from devscripts-minimal to
licensecheck and devscripts-checkbashisms. It will be removed after one
distribution release cycle, please do not reference it or depend on it in any way.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"


%install
%makeinstall_std

# Install docs through %%doc
rm -rf %{buildroot}%{_datadir}/doc

# archpath requires tla (gnu-arch) or baz (bazaar), both of which are obsolete
# and the respective Fedora packages dead. See #1128503
rm %{buildroot}%{_bindir}/archpath %{buildroot}%{_mandir}/man1/archpath*

# whodepends requires configured deb repositories
rm %{buildroot}%{_bindir}/whodepends %{buildroot}%{_mandir}/man1/whodepends*

# Create symlinks like the debian package does
ln -s %{_bindir}/cvs-debi      %{buildroot}%{_bindir}/cvs-debc
ln -s %{_bindir}/debchange     %{buildroot}%{_bindir}/dch
ln -s %{_bindir}/pts-subscribe %{buildroot}%{_bindir}/pts-unsubscribe
ln -s %{_mandir}/man1/debchange.1.gz     %{buildroot}%{_mandir}/man1/dch.1.gz
ln -s %{_mandir}/man1/pts-subscribe.1.gz %{buildroot}%{_mandir}/man1/pts-unsubscribe.1.gz

# This already is in bash-completion
rm -f %{buildroot}%{_datadir}/bash-completion/completions/bts
mkdir -p %buildroot%_sysconfdir
touch %buildroot%_sysconfdir/cvsdeb.conf


%files
%doc README
%doc --no-dereference COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{perl_vendor_privlib}/Devscripts
%exclude %{_bindir}/checkbashisms
%exclude %{_mandir}/man1/checkbashisms.1*
%config %_sysconfdir/cvsdeb.conf
%files -n python3-module-%name
%{python3_sitelibdir_noarch}/%{name}
%{python3_sitelibdir_noarch}/%{name}*.egg-info/


%files -n checkbashisms
%doc --no-dereference COPYING
%{_bindir}/checkbashisms
%{_mandir}/man1/checkbashisms.1*
%{_mandir}/man5/devscripts.conf.5*

%changelog
* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 2.19.2-alt1_1
- update to new release by fcimport

* Thu Nov 29 2018 Fr. Br. George <george@altlinux.ru> 2.18.9-alt1
- Version bump to 2.18.9

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 2.18.7-alt1_1
- new version

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.18.3-alt1_4
- update to new release by fcimport

* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.18.3-alt1_1
- new version - checkbashisms that works

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 2.15.1-alt1
- Autobuild version bump to 2.15.1

* Tue Dec 16 2014 Fr. Br. George <george@altlinux.ru> 2.14.11-alt1
- Autobuild version bump to 2.14.11

* Thu Oct 23 2014 Fr. Br. George <george@altlinux.ru> 2.14.10-alt1
- Autobuild version bump to 2.14.10

* Thu Jan 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.6-alt2.1
- Fixed build

* Wed Oct 16 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.12.6-alt2
- Fix build with new pod2man.

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 2.12.6-alt1
- Autobuild version bump to 2.12.6

* Thu Nov 15 2012 Fr. Br. George <george@altlinux.ru> 2.12.5-alt1
- Autobuild version bump to 2.12.5
- Hack in old po4a config file

* Wed Oct 24 2012 Fr. Br. George <george@altlinux.ru> 2.12.4-alt1
- Autobuild version bump to 2.12.4

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 2.12.1-alt1
- Autobuild version bump to 2.12.1

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 2.11.8-alt1
- Autobuild version bump to 2.11.8

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 2.11.6-alt1
- Autobuild version bump to 2.11.6

* Wed Feb 22 2012 Fr. Br. George <george@altlinux.ru> 2.11.4-alt1
- Autobuild version bump to 2.11.4

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 2.11.3-alt1
- Autobuild version bump to 2.11.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.11.1-alt1.1
- Rebuild with Python-2.7

* Tue Aug 30 2011 Fr. Br. George <george@altlinux.ru> 2.11.1-alt1
- Autobuild version bump to 2.11.1

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.11.0-alt3
- removed conflict with checkbashisms (integrated as subpackage)

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 2.11.0-alt2
- Implement SSL hostname check omitting

* Tue Jun 21 2011 Fr. Br. George <george@altlinux.ru> 2.11.0-alt1
- Autobuild version bump to 2.11.0

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 2.10.72-alt1
- Autobuild version bump to 2.10.72

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 2.10.71-alt1
- Autobuild version bump to 2.10.71

* Tue Feb 15 2011 Fr. Br. George <george@altlinux.ru> 2.10.70-alt1
- Autobuild version bump to 2.10.70

* Thu Dec 23 2010 Fr. Br. George <george@altlinux.ru> 2.10.69-alt1
- Initial build from deb

