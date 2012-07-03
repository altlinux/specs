Name: jcr-source
Version: 0.2.4
Release: alt1.1

Summary: JCR sources to build old Jabberd 1.4 services for Jabberd2
License: GPL
Group: Development/Other

Url: http://jabber.terrapin.com/JCR/
Source: http://jabber.terrapin.com/JCR/jcr-%version.tar.gz
Patch0: jcr-0.2.4-alt-rpm_opt_flags-makefile.patch
Patch1: jcr-0.2.4-alt-stream-close.patch
Packager: Andrei Bulava <abulava@altlinux.ru>

BuildArch: noarch

%description
This is a package with sources of Jabber Component Runtime (JCR) to build
MU-Conference or another legacy Jabberd 1.4 service for Jabberd2.

%define shortname jcr
%define fullname %shortname-%version

%prep
%setup -n %fullname
%patch0 -p1

%install
cd ..
rm -rf %shortname
mv %fullname %shortname
mkdir -p %buildroot%_usrsrc
tar cjf %buildroot%_usrsrc/%fullname.tar.bz2 %shortname
pushd %buildroot%_usrsrc
ln -s %fullname.tar.bz2 %shortname.tar.bz2
popd

%files
%_usrsrc/%fullname.tar.bz2
%_usrsrc/%shortname.tar.bz2

%changelog
* Sat Oct 30 2010 Michael Shigorin <mike@altlinux.org> 0.2.4-alt1.1
- NMU: applied patch by bp@ (closes: #11463)
- minor spec cleanup
- this package seems obsolete

* Thu Dec 15 2005 Andrei Bulava <abulava@altlinux.ru> 0.2.4-alt1
- initial build for ALT Linux (thanks to Pavel Boldin <bp@> for good starting
  points)

