Name: rpm-build-mono4
Version: 0.1.2
Release: alt1

Summary: RPM helper macros and dependency utils to build Mono packages
License: GPL
Group: Development/Other

Packager: Denis Medvedev <nbr@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: rpm >= 4.0.4-alt96.13
Conflicts: rpm-build-mono

%description
These helper macros and dependency calculation utils facilitate creation
of RPM packages containing Mono bytecode archives etc.
Based on rpm-build-mono, but for mono4.

%prep
%setup

%install
install -pD -m644 rpm-build-mono4.macros %buildroot%_rpmmacrosdir/mono4
install -pD -m755 mono4.req %buildroot%_rpmlibdir/mono4.req
ln -s mono4.req %buildroot%_rpmlibdir/monolib4.req
ln -s mono4.req %buildroot%_rpmlibdir/mono4.prov
install -pD -m755 mono4.req.files %buildroot%_rpmlibdir/mono4.req.files
ln -s mono4.req.files %buildroot%_rpmlibdir/mono4lib.req.files
install -pD -m755 mono4.prov.files %buildroot%_rpmlibdir/mono4.prov.files

%files
%_rpmmacrosdir/mono4
%_rpmlibdir/mono4*
%_rpmlibdir/monolib4*

%changelog
* Wed Nov 16 2016 Denis Medvedev <nbr@altlinux.org> 0.1.2-alt1
- Find ALL dlls under all dirs in mono directories for provides

* Wed Apr 06 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt6
- Incorporated changes from imz@ - not lib64 centered way.
More portable.

* Wed Jan 27 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt5
- Fixed searching additional direcotory for mono.configuration.security

* Wed Jan 27 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt4
- Fixed bug in provides search

* Tue Jan 26 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt3
- move req to mono4

* Sat Jan 16 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt2
- requirement for monodis removed

* Sat Jan 16 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt1
- Initial release

