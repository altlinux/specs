Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global   debug_package   %{nil}

%global   provider        github
%global   provider_tld    com
%global   project         linuxdeepin
%global   repo            go-lib
# https://github.com/linuxdeepin/go-lib
%global   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global   import_path     pkg.deepin.io/lib
%global   commit          1986cd005cf07a67d528f6cd70bfc008a5afb94c
%global   shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-deepin-go-lib
Version:        1.2.0
Release:        alt1_1
Summary:        Go bindings for Deepin Desktop Environment development
License:        GPLv3
URL:            https://%{provider_prefix}
Source0:        %{url}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
DLib is a set of Go bindings/libraries for DDE development.
Containing dbus (forking from guelfey), glib, gdkpixbuf, pulse and more.

%package devel
Group: Development/Other
Summary:        %{summary}
BuildArch:      noarch
# Required for tests
BuildRequires:  deepin-gir-generator
BuildRequires:  dbus-tools-gui
BuildRequires:  iso-codes
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  golang(github.com/BurntSushi/xgb/xproto)
BuildRequires:  golang(github.com/BurntSushi/xgbutil)
BuildRequires:  golang(github.com/BurntSushi/xgbutil/xevent)
BuildRequires:  golang(github.com/BurntSushi/xgbutil/xprop)
BuildRequires:  golang(github.com/BurntSushi/xgbutil/xwindow)
BuildRequires:  golang(golang.org/x/image/bmp)
BuildRequires:  golang(golang.org/x/image/tiff)
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  golang(gopkg.in/alecthomas/kingpin.v2)
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libcanberra)

Requires:       golang(github.com/BurntSushi/xgb/xproto)
Requires:       golang(github.com/BurntSushi/xgbutil)
Requires:       golang(github.com/BurntSushi/xgbutil/xevent)
Requires:       golang(github.com/BurntSushi/xgbutil/xprop)
Requires:       golang(github.com/BurntSushi/xgbutil/xwindow)
Requires:       golang(golang.org/x/image/bmp)
Requires:       golang(golang.org/x/image/tiff)

Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/app) = %{version}-%{release}
Provides:       golang(%{import_path}/appinfo) = %{version}-%{release}
Provides:       golang(%{import_path}/appinfo/desktopappinfo) = %{version}-%{release}
Provides:       golang(%{import_path}/arch) = %{version}-%{release}
Provides:       golang(%{import_path}/archive) = %{version}-%{release}
Provides:       golang(%{import_path}/archive/gzip) = %{version}-%{release}
Provides:       golang(%{import_path}/archive/utils) = %{version}-%{release}
Provides:       golang(%{import_path}/backlight/common) = %{version}-%{release}
Provides:       golang(%{import_path}/backlight/display) = %{version}-%{release}
Provides:       golang(%{import_path}/backlight/keyboard) = %{version}-%{release}
Provides:       golang(%{import_path}/calendar) = %{version}-%{release}
Provides:       golang(%{import_path}/calendar/lunar) = %{version}-%{release}
Provides:       golang(%{import_path}/calendar/util) = %{version}-%{release}
Provides:       golang(%{import_path}/dbus) = %{version}-%{release}
Provides:       golang(%{import_path}/dbus/interfaces) = %{version}-%{release}
Provides:       golang(%{import_path}/dbus/introspect) = %{version}-%{release}
Provides:       golang(%{import_path}/dbus/property) = %{version}-%{release}
Provides:       golang(%{import_path}/encoding/kv) = %{version}-%{release}
Provides:       golang(%{import_path}/event) = %{version}-%{release}
Provides:       golang(%{import_path}/fsnotify) = %{version}-%{release}
Provides:       golang(%{import_path}/gdkpixbuf) = %{version}-%{release}
Provides:       golang(%{import_path}/gettext) = %{version}-%{release}
Provides:       golang(%{import_path}/graphic) = %{version}-%{release}
Provides:       golang(%{import_path}/initializer) = %{version}-%{release}
Provides:       golang(%{import_path}/initializer/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/iso) = %{version}-%{release}
Provides:       golang(%{import_path}/keyfile) = %{version}-%{release}
Provides:       golang(%{import_path}/locale) = %{version}-%{release}
Provides:       golang(%{import_path}/log) = %{version}-%{release}
Provides:       golang(%{import_path}/mime) = %{version}-%{release}
Provides:       golang(%{import_path}/mobileprovider) = %{version}-%{release}
Provides:       golang(%{import_path}/notify) = %{version}-%{release}
Provides:       golang(%{import_path}/notify/dbusnotify) = %{version}-%{release}
Provides:       golang(%{import_path}/pinyin) = %{version}-%{release}
Provides:       golang(%{import_path}/polkit) = %{version}-%{release}
Provides:       golang(%{import_path}/polkit/policykit1) = %{version}-%{release}
Provides:       golang(%{import_path}/procfs) = %{version}-%{release}
Provides:       golang(%{import_path}/profile) = %{version}-%{release}
Provides:       golang(%{import_path}/proxy) = %{version}-%{release}
Provides:       golang(%{import_path}/pulse) = %{version}-%{release}
Provides:       golang(%{import_path}/sound) = %{version}-%{release}
Provides:       golang(%{import_path}/strv) = %{version}-%{release}
Provides:       golang(%{import_path}/tasker) = %{version}-%{release}
Provides:       golang(%{import_path}/timer) = %{version}-%{release}
Provides:       golang(%{import_path}/users/group) = %{version}-%{release}
Provides:       golang(%{import_path}/users/passwd) = %{version}-%{release}
Provides:       golang(%{import_path}/users/shadow) = %{version}-%{release}
Provides:       golang(%{import_path}/utils) = %{version}-%{release}
Provides:       golang(%{import_path}/xdg/basedir) = %{version}-%{release}
Provides:       golang(%{import_path}/xdg/userdir) = %{version}-%{release}
Provides:       deepin-%{repo} = %{version}-%{release}
Obsoletes:      deepin-%{repo} < %{version}-%{release}

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package unit-test-devel
Group: Development/Other
Summary:        Unit tests for %{name} package
# test subpackage tests code from devel subpackage

%description unit-test-devel
%{summary}.

This package contains unit tests for project
providing packages with %{import_path} prefix.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
install -d %{buildroot}%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.[h|c]" -or -iname "*.go" \! -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> devel.file-list.dir
    done
done
[ -s devel.file-list.dir ] && sort -u devel.file-list.dir >> devel.file-list

# testing files for this project
install -d %{buildroot}%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go" -or -iname "testdata*"); do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list
    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done

sort -u -o devel.file-list devel.file-list
sort -u -o unit-test-devel.file-list unit-test-devel.file-list

%files devel -f devel.file-list
%doc README.md
%doc LICENSE
%dir %{go_path}/src/%{import_path}/

%files unit-test-devel -f unit-test-devel.file-list
%doc README.md
%doc LICENSE

%changelog
* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- new version

