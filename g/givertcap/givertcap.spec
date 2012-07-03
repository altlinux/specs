Name: givertcap
Version: 1.0
Release: alt4.1.1

Group: System/Kernel and hardware
Summary: GIVERTCAP gives other application real-time capabilities
Summary(ru_RU.KOI8-R): Givertcap предоставляет приложениям возможность работать в режиме реального времени
License: GPL
Url: http://www.tml.hut.fi/~tilmonen/givertcap
Packager: Repocop Q. A. Robot <repocop@altlinux.org>

Source: %url/%name.c
Source1: givertcap.html
Source2: http://ftp.kernel.org/pub/linux/libs/security/linux-privs/kernel-2.4/capfaq-0.2.txt
Patch: %name-1.0-ccrma.patch

# Automatically added by buildreq on Mon Jul 14 2003
BuildRequires: gcc-c++ libcap-devel libstdc++-devel

%description
With the aid of givertcap you can run real-time applications (audio and
video- processing apps for example) with high priority without running
the application as root. Your application does get a collection
capabilities that allow it to run at very high priority. Givertcap was
created to overcome the lack of capability support in Linux file
systems. Once the Linux file systems start to have the necessary
functions themselves, this apps becomes unnecessary.

%description -l ru_RU.KOI8-R
При помощи givertcap вы можете запускать требующие real-time режима 
приложения с высоким приоритетом без прав суперпользователя. Когда-нибудь, 
когда файловые системы для Linux начнуть предоставлять нужную 
функциональность сами по себе, необходимость в givertcap отомрёт 
естественным образом.

# We want to limit the number of people who can access this application.
%define GROUP rtusers

%prep
%setup -T -c %name-%version
%__cp %SOURCE0 $RPM_BUILD_DIR/%name-%version
%patch -p1

%build
%__cxx $RPM_OPT_FLAGS %name.c -o %name -lcap

%install
%__install -pD %name %buildroot%_bindir/%name
%__install -d %buildroot%_docdir/%name-%version
%__install -pD -m644 %SOURCE1 %SOURCE2 %buildroot%_docdir/%name-%version

# Applications using %name needs environment variable GIVERTCAP.
cat << EOF >%name.sh
#!/bin/sh
GIVERTCAP="%_bindir/%name"
export GIVERTCAP
EOF

cat << EOF >%name.csh
#!/bin/csh
setenv GIVERTCAP "%_bindir/%name"
EOF

%__install -d %buildroot%_sysconfdir/profile.d
%__install -pD -m755 %name.sh %name.csh %buildroot%_sysconfdir/profile.d

%pre
# We need to create group %GROUP
%_sbindir/groupadd -r -f %GROUP ||:

%files
%attr(4710,root,%GROUP) %_bindir/%name
%_docdir/%name-%version/*
%_sysconfdir/profile.d/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/givertcap-%version 

%changelog
* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4.1.1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for givertcap

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt4.1
- Rebuilt with libstdc++.so.6.

* Mon Jul 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0-alt4
- Patch from CCRMA muse package.

* Tue Oct 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0-alt3
- Rebuild with gcc-3.2.

* Mon Apr 1 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0-alt2
- build process optimization.

* Mon Dec 2 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.0-alt1
- First build for Sisyphus
