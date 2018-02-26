
Name: libnss-fallback
Version: 0.0.1
Release: alt2

Summary: NSS library module for localhost fallback
License: GPL
Group: System/Libraries

Url: http://www.altlinux.org/Projects/libnss_fallback
Source: %name-%version.tar
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

BuildRequires: gcc-c++ cmake

Requires(pre): chrooted >= 0.3.6-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.6-alt1 sed

%description
NSS library module for localhost fallback

%prep
%setup %name-%version

%build
mkdir build
cd build
cmake ../ \
        -DCMAKE_INSTALL_PREFIX=/ \
%if %_lib == lib64
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_BUILD_TYPE="Release"
#        -DCMAKE_SKIP_RPATH=YES

%make_build VERBOSE=1

%install
cd build
%makeinstall DESTDIR=%buildroot

%post
if [ "$1" = "1" ]; then
    grep -q '^hosts:[[:blank:]]*\(.\+[[:blank:]]\+\)*fallback\($\|[[:blank:]]\)' \
        /etc/nsswitch.conf || \
    sed -i.rpmorig -e 's/^\(hosts:.\+\)$/\1 fallback/g' \
        /etc/nsswitch.conf
fi
update_chrooted all

%postun
if [ "$1" = "0" ]; then
    sed -i -e 's/^hosts:fallback/hosts:/g' \
           -e 's/^\(hosts:\)\(.\+[[:blank:]]*\)*[[:blank:]]\+fallback\($\|[[:blank:]].*\)$/\1\2\3/g' \
        /etc/nsswitch.conf
fi
update_chrooted all

%files
/%_lib/*.so.*

%changelog
* Thu Feb 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt2
- Add automatic module configurtion during installation process

* Sat Nov 22 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt1
- Initial first release for testing
