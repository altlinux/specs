Name: e3
Version: 2.8.0
Release: alt3
Group: System/Base
Summary: e3 is tiny wordstar/emacs/pico/vi/nedit alike editor, well suited for rescue disks
License: GPL
Source: %name-%version.tar
Url: http://freshmeat.net/projects/e3

Packager: Lenar Shakirov <snejok@altlinux.org>

Patch: e3.makefile.patch

# Automatically added by buildreq on Tue Dec 12 2006
BuildRequires: nasm

%description
e3 is teeny tiny editor that doesn't depend on any libs.
e3 uses subset of wordstar|emacs|pico|vi|nedit commands.
Author: Albrecht Kleine  <kleine@ak.sax.de>

%prep
%setup
%patch0

%build
%ifarch x86_64
make 64
%else
%ifarch i586
make
%endif
%endif

%install
make PREFIX="%buildroot" MANDIR="%buildroot%_man1dir" install
cd %buildroot/bin
rm -f %name[enpvw]*
for i in e3em e3ne e3pi e3vi e3ws
do
ln -s %name $i
done

%files
/bin/%{name}*
%_man1dir/%{name}*

%changelog
* Tue Oct 04 2011 Lenar Shakirov <snejok@altlinux.ru> 2.8.0-alt3
- removed set_strip_method macro (rpm-4.0.4-alt100.36)

* Tue Dec 21 2010 Lenar Shakirov <snejok@altlinux.ru> 2.8.0-alt2
- e3.makefile.patch added

* Tue Dec 21 2010 Lenar Shakirov <snejok@altlinux.ru> 2.8.0-alt1
- new version

* Mon Aug 02 2010 Lenar Shakirov <snejok@altlinux.ru> 2.7.1-alt3
- 'make nasm64' on x86_64

* Sun Jul 18 2010 Lenar Shakirov <snejok@altlinux.ru> 2.7.1-alt2
- packages-info-i18n-common deleted from BuildReqs

* Fri Mar 26 2010 Lenar Shakirov <snejok@altlinux.ru> 2.7.1-alt1
- new version

* Fri Mar 26 2010 Lenar Shakirov <snejok@altlinux.ru> 2.7.0-alt3
- Source: tar.gz -> tar

* Fri Mar 26 2010 Lenar Shakirov <snejok@altlinux.ru> 2.7.0-alt2
- URL updated
- .gear-rules -> .gear/rules
- packager - Me
- Spec cleanup (thanks to rpmcs)

* Tue Dec 12 2006 Terechkov Evgenii <evg@altlinux.ru> 2.7.0-alt1
- Initial build for Sisyphus
