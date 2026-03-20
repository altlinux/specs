%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lfs=relaxed

Name: firejail
Version: 0.9.80
Release: alt1
Summary: Linux namespaces sandbox program
License: GPLv2+
Group: Development/Tools
Url: https://firejail.wordpress.com/
VCS: https://github.com/netblue30/firejail.git
Source: %name-%version.tar
Patch1: %name-0.9.78-alt-skip-unreadable-private-etc.patch
Patch2: %name-0.9.78-alt-whitelist-sandbox-users.patch
Patch3: %name-0.9.80-alt-firecfg-path-warning.patch

BuildRequires(pre): rpm-build-python3

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces. It includes a sandbox profile for Mozilla Firefox.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README* RELNOTES COPYING
%attr(4711, root, root) %_bindir/%name
%_bindir/firecfg
%_bindir/firemon
%_bindir/jailcheck
%_libdir/%name
%_datadir/gtksourceview-*/language-specs/firejail-profile.lang
%_datadir/bash-completion/completions/%name
%_datadir/bash-completion/completions/firecfg
%_datadir/bash-completion/completions/firemon
%_datadir/zsh/site-functions/_firejail
%_datadir/vim/vimfiles/ftdetect/%name.vim
%_datadir/vim/vimfiles/ftplugin/%name.vim
%_datadir/vim/vimfiles/syntax/%name.vim
%exclude %_docdir/%name
%_man1dir/%name.1*
%_man1dir/firecfg.1*
%_man1dir/firemon.1*
%_man1dir/jailcheck.1*
%_man5dir/%name-login.5*
%_man5dir/%name-profile.5*
%_man5dir/%name-users.5*
%config %_sysconfdir/%name

%changelog
* Fri Mar 20 2026 Anton Farygin <rider@altlinux.org> 0.9.80-alt1
- 0.9.78 -> 0.9.80
- firecfg: warn when symlinks won't intercept commands
  due to PATH order (closes: #58210)

* Thu Mar 05 2026 Anton Farygin <rider@altlinux.org> 0.9.78-alt3
- skip unreadable files in private-etc instead of crashing (closes: #58112)
- sandbox user isolation: only expose root, nobody and current user instead of
  using UID_MIN/GID_MIN threshold from /etc/login.defs (closes: #45710)
- removed login.defs from default private-etc list (no longer needed at runtime)

* Tue Feb 24 2026 Anton Farygin <rider@altlinux.org> 0.9.78-alt2
- set SUID bit on firejail binary (Closes: #57987)
- enabled user namespace support (--noroot option)

* Fri Jan 09 2026 Anton Farygin <rider@altlinux.org> 0.9.78-alt1
- 0.9.76 -> 0.9.78

* Sun Sep 14 2025 Anton Farygin <rider@altlinux.com> 0.9.76-alt1
- 0.9.74 -> 0.9.76

* Mon Mar 31 2025 Anton Farygin <rider@altlinux.com> 0.9.74-alt1
- 0.9.72 -> 0.9.74

* Tue Mar 21 2023 Anton Farygin <rider@altlinux.ru> 0.9.72-alt1
- 0.9.68 -> 0.9.72 (Fixes: CVE-2022-31214)

* Wed Feb 16 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.68-alt1
- Updated to upstream version 0.9.68.

* Tue Jul 27 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.66-alt1
- Updated to upstream version 0.9.66.

* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.64.4-alt2
- Updated build dependencies.

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.64.4-alt1
- Updated to upstream version 0.9.64.4.

* Thu Feb 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.64.2-alt1
- Updated to upstream version 0.9.64.2.

* Mon Oct 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.64-alt1
- Updated to upstream version 0.9.64.

* Wed Aug 19 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.62.4-alt1
- Updated to upstream version 0.9.62.4 (Fixes: CVE-2020-17367, CVE-2020-17368).

* Fri Apr 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.62-alt1
- Updated to upstream version 0.9.62.

* Wed Jan 10 2018 Anton Midyukov <antohami@altlinux.org> 0.9.52-alt1
- new version 0.9.52

* Mon Nov 06 2017 Anton Midyukov <antohami@altlinux.org> 0.9.50-alt2
- Remove requires bash-completion (Closes: 34128)

* Thu Oct 26 2017 Anton Midyukov <antohami@altlinux.org> 0.9.50-alt1
- new version 0.9.50

* Tue Jul 25 2017 Anton Midyukov <antohami@altlinux.org> 0.9.48-alt1
- new version 0.9.48

* Tue May 23 2017 Anton Midyukov <antohami@altlinux.org> 0.9.46-alt1
- new version 0.9.46

* Mon May 08 2017 Anton Midyukov <antohami@altlinux.org> 0.9.44.10-alt1
- new version 0.9.44.10
- remove identical files (Closes: 33458)

* Tue Jan 31 2017 Anton Midyukov <antohami@altlinux.org> 0.9.44.8-alt1
- new version 0.9.44.8

* Sun Jan 08 2017 Anton Midyukov <antohami@altlinux.org> 0.9.44.4-alt1
- new version 0.9.44.4
- Update for release with security fixes:
- CVE-2017-5207 (-bandwidth root shell found by Martin Carpenter)
- CVE-2017-5206 (disabled --allow-debuggers when running on kernel 4.8)
- CVE-2017-5180 (root exploit found by Sebastian Krahmer)

* Fri Jan 06 2017 Anton Midyukov <antohami@altlinux.org> 0.9.44.2-alt1
- Initial build for ALT Linux Sisyphus.
