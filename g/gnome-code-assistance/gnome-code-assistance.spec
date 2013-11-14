%define _libexecdir %_prefix/libexec
%define ver_major 0.3

%def_enable c
%def_enable python
%def_disable ruby
%def_disable css
%def_enable js
%def_enable xml
%def_enable vala
%def_enable go

Name: gnome-code-assistance
Version: %ver_major.0
Release: alt1

Summary: GNOME Code Assistance Service
License: GPL
Group: Graphical desktop/GNOME
Url: https://git.gnome.org/browse/gnome-code-assistance

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_compile_include %_libexecdir/%name

# it's especially for golang
%add_verify_elf_skiplist %_libexecdir/%name/go
%add_debuginfo_skiplist %_libexecdir/%name/go
%brp_strip_none %_libexecdir/%name/go

# From configure.ac
%define glib_ver 2.36
%define pygobject_ver 2.38
%define llvm_ver 2.8
%define ruby_ver 2.0
%define vala_ver 0.20

BuildPreReq: rpm-build-gnome

# From configure.in
BuildRequires: libgio-devel >= %glib_ver rpm-build-python3 python3-module-dbus python-module-dbus-devel
BuildRequires: python3-module-pygobject3-devel >= %pygobject_ver
%{?_enable_c:BuildRequires: llvm-devel >= %llvm_ver}
%{?_enable_ruby:BuildRequires: ruby >= %ruby_ver}
%{?_enable_css:BuildRequires: ruby >= %ruby_ver}
%{?_enable_js:BuildRequires: libgjs}
%{?_enable_vala:BuildRequires: libgee0.8-devel libvala-devel >= %vala_ver vala-tools}
%{?_enable_go:BuildRequires: golang}

%description
gnome-code-assistance is a project which aims to provide common code
assistance services for code editors (simple editors as well as IDEs).
It is an effort to provide a centralized code-assistance as a service
for the GNOME platform instead of having every editor implement their
own solution.

%prep
%setup

%build
%configure \
    --disable-static \
    %{subst_enable c} \
    %{subst_enable python} \
    %{subst_enable ruby} \
    %{subst_enable css} \
    %{subst_enable js} \
    %{subst_enable xml} \
    %{subst_enable vala} \
    %{subst_enable go}

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%dir %_libexecdir/%name
%_libexecdir/%name/
%{?_enable_c:%_datadir/dbus-1/services/org.gnome.CodeAssist.v1.c.service}
%{?_enable_css:%_datadir/dbus-1/services/org.gnome.CodeAssist.v1.css.service}
%{?_enable_go:%_datadir/dbus-1/services/org.gnome.CodeAssist.v1.go.service}
%{?_enable_js:%_datadir/dbus-1/services/org.gnome.CodeAssist.v1.js.service}
%{?_enable_python:%_datadir/dbus-1/services/org.gnome.CodeAssist.v1.python.service}
%{?_enable_ruby:%_datadir/dbus-1/services/org.gnome.CodeAssist.v1.ruby.service}
%_datadir/dbus-1/services/org.gnome.CodeAssist.v1.sh.service
%{?_enable_vala:%_datadir/dbus-1/services/org.gnome.CodeAssist.v1.vala.service}
%{?_enable_xml:%_datadir/dbus-1/services/org.gnome.CodeAssist.v1.xml.service}
%_datadir/glib-2.0/schemas/org.gnome.codeassistance.gschema.xml
%doc AUTHORS README NEWS

%changelog
* Thu Nov 14 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first build for Sisyphus

