%define bname qaccessibilityclient
Name: lib%bname-qt5
Version: 0.4.0
Release: alt1

Summary: This library is used when writing accessibility clients
License: LGPLv2.1
Group: System/Libraries
Url: https://cgit.kde.org/libqaccessibilityclient.git
Source0: %name-%version.tar

# Automatically added by buildreq on Thu Mar 21 2019 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ gem-power-assert gem-setup glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-test libqt5-widgets libsasl2-3 libstdc++-devel python-base python-modules python3 python3-base rpm-build-python3 rpm-build-ruby ruby ruby-bundler ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
#BuildRequires: asciidoctor extra-cmake-modules gem-did-you-mean libssl-devel python3-dev qt5-base-devel ruby-minitest ruby-net-telnet ruby-rubygems-update ruby-test-unit ruby-xmlrpc
BuildRequires(pre): rpm-build-ubt
BuildRequires: extra-cmake-modules
BuildRequires: cmake qt5-base-devel

%description
%summary.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: libqaccessibilityclient-devel
%description devel
%summary.

%prep
%setup
#exclude tests and examples from build
sed -i '/add_subdirectory.*tests\|add_subdirectory.*examples/d' ./CMakeLists.txt

%build
%cmake \
	-DQT4_BUILD=OFF \
	#
%cmake_build

%install
%cmakeinstall_std

%files
%doc COPYING* AUTHORS ChangeLog
%_libdir/%{name}.so.0
%_libdir/%{name}.so.*

%files devel
%_includedir/%{bname}/
%_libdir/cmake/QAccessibilityClient/
%_libdir/%{name}.so

%changelog
* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Mon Dec 25 2017 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt2%ubt
- track library soname

* Fri Aug 25 2017 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1%ubt
- Initial build
