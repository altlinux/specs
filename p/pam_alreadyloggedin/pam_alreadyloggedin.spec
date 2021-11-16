%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_without libpam
%def_with    libpam0
%def_without libpam2

%define pamconfdir   %_sysconfdir/pam.d
%define pamlibdir    /%_lib/security

%ifdef add_findprov_lib_path
%add_findprov_lib_path %pamlibdir
%endif

Name: pam_alreadyloggedin
Version: 0.3.2
Release: alt5
Summary: Skip password authorization if user is already logged in
Summary(ru_RU.UTF-8): Вход в систему без пароля, если уже выполнен вход с другой консоли
License: BSD-3-Clause
Group: System/Base
Url: http://ilya-evseev.narod.ru/posix/%name

Source: %name-%version.tar

%if_with libpam
BuildRequires: libpam-devel
%endif
%if_with libpam0
BuildRequires: libpam0-devel
%endif
%if_with libpam2
BuildRequires: libpam2-devel
%endif

%description
Based on the appropriate module from FreeBSD project source tree,
%name is a PAM module which allows you to skip
authorization stuff (like password entering, etc.),
if you are already logged in on the another console.
See using example in %_defaultdocdir/%name-%version/examples directory.

%description -l ru_RU.UTF-8
%name является модулем PAM, который позволяет пользователю
пропускать ввод пароля при входе в систему,
если этот пользователь уже зашёл в систему с другой консоли.

Данный модуль не начинает использоваться немедленно при инсталляции;
пример политики PAM для его подключения смотрите в каталоге
%_defaultdocdir/%name-%version/examples.

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%make_build

%install
%make_install install FAKEROOT=%buildroot MAN8DIR=%_man8dir SECUREDIR=/%_lib/security

mkdir examples
install -pD -m644 login.sso examples/login
sed -i -e 's:/lib/security/::g' examples/login

rm -f %buildroot%pamconfdir/login.sso

%files
%doc examples
%pamlibdir/%name.so
%_man8dir/%name.8*

%changelog
* Tue Nov 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt5
- Fixed build, linking and enabled debuginfo.

* Fri Apr 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt4
- Fixed license.

* Tue Jan 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt3
- Fixed pam module location (Closes: #35894)
- Changed package summary and description translation to UTF-8
- Updated description and example config

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt2
- Fixed spec to allow any man page compression

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.2-alt1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * docdir-is-not-owned for pam_alreadyloggedin

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.2-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Wed Nov 22 2006 Ilya Evseev <evseev@altlinux.ru> 0.3.2-alt1
- prevent gcc4 stack protection problem: http://wiki.sisyphus.ru/devel/gcc4
- include syslog.h to sources

* Fri Oct  7 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.3.1-alt1
- bugfix in 0.3.1: explicitly include syslog headers in debug mode.
- handle libpam-devel alternatives in Sisyphus,
  use "rpmbuild --with libpam" for getting old functionality.
- new feature in 0.3.1 makefile: added targets "archive", "rpm".

* Sun Nov 28 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.3-alt1
- version 0.3: patch from Luca Benini <lbenini@csr.unibo.it>
  for skipping some checks no more actual for Linux
- specfile warning about unused policy installed in %pamconfdir

* Wed Aug  4 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.2-alt4
- added add_findprov_lib_path macro
- login.sso is moved from /etc/pam.d to docdir/examples,
  comments are no more needed.

* Tue Jul  6 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.2-alt3
- fixups in login.sso for preventing invalid RPM requirements
- source archive format is changed from ZIP to tar.gz

* Fri Jul  2 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.2-alt2
- specfile cleanups before adding to ALTLinux Sisyphus repository
- added russian summary and description

* Wed Jan 28 2004 Ilya G. Evseev <ilya_evseev@mail.ru> 0.2-1
- Initial build, based on the FreeBSD's module version 0.2

## EOF ##
