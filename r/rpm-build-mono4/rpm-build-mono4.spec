Name: rpm-build-mono4
Version: 0.1.1
Release: alt2

Summary: RPM helper macros and dependency utils to build Mono packages
License: GPL
Group: Development/Other

Packager: Denis Medvedev <nbr@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: rpm >= 4.0.4-alt96.13
Conflicts: rpm-build-mono

%description
These helper macros and dependency calculation utils facilitate creation of
RPM packages containing Mono bytecode archives etc.
Based on rpm-build-mono, but for mono4.

%prep
%setup

%install
install -pD -m644 rpm-build-mono.macros %buildroot%_rpmmacrosdir/mono
install -pD -m755 mono.req %buildroot%_rpmlibdir/mono.req
ln -s mono.req %buildroot%_rpmlibdir/monolib.req
ln -s mono.req %buildroot%_rpmlibdir/mono.prov
install -pD -m755 mono.req.files %buildroot%_rpmlibdir/mono.req.files
ln -s mono.req.files %buildroot%_rpmlibdir/monolib.req.files
install -pD -m755 mono.prov.files %buildroot%_rpmlibdir/mono.prov.files

%files
%_rpmmacrosdir/mono
%_rpmlibdir/mono*

%changelog
* Sat Jan 16 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt2
- requirement for monodis removed

* Sat Jan 16 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt1
- Initial release

