Name: firejail
Version: 0.9.52
Release: alt1
Summary: Linux namepaces sandbox program

License: GPLv2+
Group: Development/Tools
Source: %name-%version.tar
Url: http://github.com/netblue30/firejail

Packager: Anton Midyukov <antohami@altlinux.org>

%description
Firejail  is  a  SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces. It includes a sandbox profile for Mozilla Firefox.

%prep
%setup

%build
%configure --disable-userns
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README* RELNOTES COPYING
%_bindir/%name
%_bindir/firecfg
%_bindir/firemon
%_libdir/%name
%_datadir/bash-completion/completions/%name
%_datadir/bash-completion/completions/firecfg
%_datadir/bash-completion/completions/firemon
%exclude %_docdir/%name
%_man1dir/%name.1.*
%_man1dir/firecfg.1.*
%_man1dir/firemon.1.*
%_man5dir/%name-login.5.*
%_man5dir/%name-profile.5.*
%config %_sysconfdir/%name


%changelog
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
