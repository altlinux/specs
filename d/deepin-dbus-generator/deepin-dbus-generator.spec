Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global repo go-dbus-generator

Name:           deepin-dbus-generator
Version:        0.6.6
Release:        alt1_3
Summary:        Convert dbus interfaces to go-lang or qml wrapper code
License:        GPLv3+
URL:            https://github.com/linuxdeepin/go-dbus-generator
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
BuildRequires:  golang
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  golang(pkg.deepin.io/lib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Qml)
Source44: import.info

%description
Static dbus binding generator for dlib.

%prep
%setup -q -n %{repo}-%{version}
# qmake path
sed -i 's|qmake|qmake-qt5|' build_test.go template_qml.go

%build
export GOPATH="%{go_path}"
BUILD_ID="0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"
function gobuild { go build -a -ldflags "-B $BUILD_ID" -v -x "$@"; }
gobuild -o dbus-generator

%install
install -Dm755 dbus-generator %{buildroot}%{_bindir}/dbus-generator

%files
%doc README.md
%doc --no-dereference LICENSE
%{_bindir}/dbus-generator

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt1_3
- update to new release by fcimport

* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt1_1
- new version

