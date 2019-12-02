Name: opencaster
Version: 3.2.1
Release: alt2
Summary: MPEG transport stream generation and management tools
Group: Networking/Other

Packager: Alexei Takaseev <taf@altlinux.ru>

License: GPLv2
Url: http://avalpa.com/the-key-values/15-free-software/33-opencaster
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Thu Oct 02 2014
# optimized out: libcloog-isl4 python-base python-modules python-modules-compiler python-modules-email
BuildRequires: libdvbcsa-devel python-devel zlib-devel

%description
Free DVB TS server software useful for many purposes: carousel server,
PSI table generator, datacasting, MPEG2 "poor man" playout system.
Avalpa OpenCaster is a collection of tools that is able to generate an
MPEG-2 data structure (stored within a Transport Stream file).
Therefore it can can also manipulate the inside packets (video, audio,
teletext packets but also Service Information/Program Specific
Information ones).

%package -n python-module-opencaster
Summary: Python libraries for the OpenCaster
Group: Development/Python
License: LGPLv2
%description -n python-module-opencaster
This package contains Python libraries for OpenCaster.

%prep
%setup
%patch0 -p1

find -iname "*.py" -exec sed -i 's@/usr/bin/env python@/usr/bin/env python2.7@g' '{}' ';'

%build
%make_build

pushd tools/tscrypt
    %make_build
popd

# ip2sec, oddparity

%install
install -d %buildroot%_bindir
make -C tools install DESTDIR=%buildroot%_bindir
make -C tools/tscrypt install DESTDIR=%buildroot%_bindir

cd libs/dvbobjects
%__python setup.py install --optimize=2 --root=%buildroot

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %_bindir/*

%files -n python-module-opencaster
%python_sitelibdir/*

%changelog
* Mon Dec 02 2019 Alexei Takaseev <taf@altlinux.org> 3.2.1-alt2
- Fix build with python 2.7

* Thu Oct 02 2014 Alexei Takaseev <taf@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus
