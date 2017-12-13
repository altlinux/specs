Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global   debug_package   %{nil}

%global   provider        github
%global   provider_tld    com
%global   project         BurntSushi
%global   repo            xgbutil
# https://github.com/BurntSushi/xgbutil
%global   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global   import_path     %{provider_prefix}
%global   commit          f7c97cef3b4e6c88280a5a7091c3314e815ca243
%global   shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.1.git%{shortcommit}
Summary:        XGB is the X protocol Go language Binding
License:        WTFPL
URL:            https://%{provider_prefix}
Source0:        %{url}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}.

%package devel
Group: Development/Other
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  golang(github.com/BurntSushi/freetype-go/freetype)
BuildRequires:  golang(github.com/BurntSushi/freetype-go/freetype/truetype)
BuildRequires:  golang(github.com/BurntSushi/graphics-go/graphics)
BuildRequires:  golang(github.com/BurntSushi/xgb)
BuildRequires:  golang(github.com/BurntSushi/xgb/shape)
BuildRequires:  golang(github.com/BurntSushi/xgb/xinerama)
BuildRequires:  golang(github.com/BurntSushi/xgb/xproto)
Requires:       golang(github.com/BurntSushi/freetype-go/freetype)
Requires:       golang(github.com/BurntSushi/freetype-go/freetype/truetype)
Requires:       golang(github.com/BurntSushi/graphics-go/graphics)
Requires:       golang(github.com/BurntSushi/xgb)
Requires:       golang(github.com/BurntSushi/xgb/shape)
Requires:       golang(github.com/BurntSushi/xgb/xinerama)
Requires:       golang(github.com/BurntSushi/xgb/xproto)
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/ewmh) = %{version}-%{release}
Provides:       golang(%{import_path}/gopher) = %{version}-%{release}
Provides:       golang(%{import_path}/icccm) = %{version}-%{release}
Provides:       golang(%{import_path}/keybind) = %{version}-%{release}
Provides:       golang(%{import_path}/motif) = %{version}-%{release}
Provides:       golang(%{import_path}/mousebind) = %{version}-%{release}
Provides:       golang(%{import_path}/xcursor) = %{version}-%{release}
Provides:       golang(%{import_path}/xevent) = %{version}-%{release}
Provides:       golang(%{import_path}/xgraphics) = %{version}-%{release}
Provides:       golang(%{import_path}/xinerama) = %{version}-%{release}
Provides:       golang(%{import_path}/xprop) = %{version}-%{release}
Provides:       golang(%{import_path}/xrect) = %{version}-%{release}
Provides:       golang(%{import_path}/xwindow) = %{version}-%{release}

%description devel
%{summary}.

xgbutil is a utility library designed to work with the X Go Binding. This
project's main goal is to make various X related tasks easier. For example,
binding keys, using the EWMH or ICCCM specs with the window manager,
moving/resizing windows, assigning function callbacks to particular events,
drawing images to a window, etc.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.


%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
install -d -p %{buildroot}%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
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
sort -u devel.file-list.dir >> devel.file-list

sort -u -o devel.file-list devel.file-list

%files devel -f devel.file-list
%doc README
%doc COPYING
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.1.gitf7c97ce
- new version

