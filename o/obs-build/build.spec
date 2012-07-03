#
# spec file for package build
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
 
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
 
# norootforbuild

%define altlinux 1 

%if 0%{?altlinux}
%define _perl_lib_path %buildroot%_libexecdir/%name
%endif
 
Name:           obs-build
License:        GPLv2+
Group:          Development/Tools
#AutoReqProv:    on
Summary:        A Script to Build SUSE Linux RPMs
Version:        2012.03.06
Release:        alt1

Packager: Denis Pynkin <dans@altlinux.org>

#!BuildIgnore:  build-mkbaselibs
Source:         obs-build-%{version}.tar.gz
#BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# Manual requires to avoid hard require to bash-static
AutoReqProv:    off
# Keep the following dependencies in sync with obs-worker package
Requires:       bash
Requires:       perl
Requires:       binutils
Requires:       tar
Conflicts:      bsdtar < 2.5.5
%if 0%{?suse_version} > 1000
# None of them are actually required for core features.
# Perl helper scripts use them.
Recommends:     perl(Date::Language)
Recommends:     perl(Date::Parse)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(Pod::Usage)
Recommends:     perl(Time::Zone)
Recommends:     perl(URI)
Recommends:     perl(XML::Parser)
Recommends:     bsdtar
%endif

%if 0%{?altlinux}
Requires: perl(Data/Dumper.pm)  
Requires: perl(Date/Language.pm)  
Requires: perl(Date/Parse.pm)  
Requires: perl(Digest/MD5.pm)  
Requires: perl(Encode.pm)  
Requires: perl(File/Basename.pm)  
Requires: perl(File/Path.pm)  
Requires: perl(File/Temp.pm)  
Requires: perl(Getopt/Long.pm)  
Requires: perl(IO/Uncompress/Gunzip.pm)  
Requires: perl(LWP/UserAgent.pm)  
Requires: perl(POSIX.pm)  
Requires: perl(Pod/Usage.pm)  
Requires: perl(Time/Zone.pm)  
Requires: perl(URI.pm)  
Requires: perl(XML/Parser.pm)
Requires: obs-build-mkbaselibs
%else
%if 0%{?suse_version} > 1120 || ! 0%{?suse_version}
Requires:       build-mkbaselibs
%endif
%endif
 
%if 0%{?suse_version} > 1120 || 0%{?mdkversion}
Recommends:     build-mkdrpms
%endif
 
%description
This package provides a script for building RPMs for SUSE Linux in a
chroot environment.
 
 
%if 0%{?suse_version} > 1120 || ! 0%{?suse_version}
 
%package mkbaselibs
License:        GPLv2+
Group:          Development/Tools
Summary:        Tools to generate base lib packages
# NOTE: this package must not have dependencies which may break boot strapping (eg. perl modules)
 
%description mkbaselibs
This package contains the parts which may be installed in the inner build system
for generating base lib packages.

%if !0%{?altlinux}
%package mkdrpms
License:        GPLv2+
Group:          Development/Tools
Summary:        Tools to generate delta rpms
Requires:       deltarpm
# XXX: we wanted to avoid that but mkdrpms needs Build::Rpm::rpmq
Requires:       build
 
%description mkdrpms
This package contains the parts which may be installed in the inner build system
for generating delta rpm packages.
%endif
%endif

%prep
%setup -q -n obs-build-%version

%build

%install
make DESTDIR=$RPM_BUILD_ROOT install
%if 0%{?sles_version} < 12
 # use sle variation with IA64 compat package generation
 install -m 0644 baselibs_global-sle.conf \
                $RPM_BUILD_ROOT/usr/lib/build/baselibs_global.conf
%endif
cd $RPM_BUILD_ROOT/usr/lib/build/configs/
%if 0%{?suse_version}
%if 0%{?sles_version}
 ln -s sles%{sles_version}.conf default.conf
%else
 V=%suse_version
 ln -s sl${V:0:2}.${V:2:1}.conf default.conf
%endif
test -e default.conf
%endif
 
%files
%defattr(-,root,root)
%doc README
/usr/bin/build
/usr/bin/buildvc
/usr/bin/unrpm
/usr/lib/build
%{_mandir}/man1/build.1*

%if 0%{?suse_version} > 1120 || ! 0%{?suse_version}
%exclude /usr/lib/build/mkbaselibs
%exclude /usr/lib/build/baselibs*
%if !0%{?altlinux}
%exclude /usr/lib/build/mkdrpms
%endif

%files mkbaselibs
%defattr(-,root,root)
%dir /usr/lib/build
/usr/lib/build/mkbaselibs
/usr/lib/build/baselibs*

%if !0%{?altlinux}
%files mkdrpms
%defattr(-,root,root)
%dir /usr/lib/build
/usr/lib/build/mkdrpms
%endif
%endif

%changelog
* Mon Apr 02 2012 Denis Pynkin <dans@altlinux.org> 2012.03.06-alt1
- New version

* Fri Oct 28 2011 Denis Pynkin <dans@altlinux.org> 2011.10.25-alt1
- first build for ALTLinux
- fix for alt rpm 
- added 'newinstance' option during devpts mount

* Tue Oct 25  2011 - <adrian@suse.de> 2011.10.25-0
- use github.com as git repo now
- fix build for rpmv5

