Name: myMPD
Version: 10.1.6
Release: alt1

Summary: myMPD is a standalone and mobile friendly web mpd client with a tiny footprint and advanced features
License: GPL-3.0-or-later
Group: Sound

Url: https://github.com/jcorporation/myMPD
# repacked https://github.com/jcorporation/%name/archive/refs/tags/v%version.tar.gz
Source0: %name-%version.tar
Source1: mympd.init

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc
BuildRequires: cmake
BuildRequires: perl
BuildRequires: jq
BuildRequires: libssl-devel
BuildRequires: libid3tag-devel
BuildRequires: libflac-devel
BuildRequires: liblua5.3-devel
BuildRequires: libpcre2-devel

%description
myMPD is a standalone and lightweight web-based MPD client.
It's tuned for minimal resource usage and requires only very few dependencies.
Therefore myMPD is ideal for raspberry pis and similar devices.

%prep
%setup
%ifarch %e2k
sed -i "s/-Werror /-Wno-error /" {,test/}CMakeLists.txt
%endif

%build
 ./build.sh createassets
cd release || exit 1
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_BUILD_TYPE=RELEASE ..
make

%install
cd release || exit 1
%makeinstall_std
install -pDm755 %SOURCE1 %buildroot/%_initdir/mympd

%pre
if [ $1 = 1 ]; then
# Add the "mympd" user and group
    getent group mympd > /dev/null || groupadd -r mympd
    getent passwd mympd > /dev/null || \
        useradd -r -g mympd -s /sbin/nologin -d /var/lib/mympd mympd
fi

%files
%defattr(-,root,root,-)
%doc README.md LICENSE.md
%_bindir/mympd
%_bindir/mympd-script
%_unitdir/mympd.service
%_initdir/mympd
%_man1dir/mympd.1.xz
%_man1dir/mympd-script.1.xz

%changelog
* Sun Dec 11 2022 Nikolay Burykin <bne@altlinux.org> 10.1.6-alt1
- 10.1.6 

* Tue Oct 18 2022 Nikolay Burykin <bne@altlinux.org> 9.5.0-alt1
- 9.5.0

* Thu Aug 18 2022 Nikolay Burykin <bne@altlinux.org> 9.4.1-alt1
- 9.4.1

* Thu Jun 16 2022 Nikolay Burykin <bne@altlinux.org> 9.3.4-alt1
- 9.3.4

* Mon Jun 06 2022 Nikolay Burykin <bne@altlinux.org> 9.3.3-alt1
- 9.3.3

* Fri May 20 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 9.3.1-alt1.1
- Fixed build for Elbrus

* Wed May 11 2022 Nikolay Burykin <bne@altlinux.org> 9.3.1-alt1
- Initial build for Sisyphus
