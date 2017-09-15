# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/python pkgconfig(glib-2.0)
# END SourceDeps(oneline)
BuildRequires: xvfb-run
%define _libexecdir %_prefix/libexec
%define oldname caja-dropbox
%define fedora 25
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.16

Summary: 		Dropbox extension for caja
Name: 			mate-file-manager-dropbox
Version: 		1.18.0
Release: 		alt1_2
License: 		GPLv2+
Group: 			Graphical desktop/MATE
URL: 			http://git.mate-desktop.org/%{oldname}
Source0: 		http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz

ExclusiveArch:  i686 x86_64

BuildRequires:  mate-file-manager-devel
%if 0%{?fedora} >= 26
BuildRequires:  python-module-docutils python-module-docutils-compat
%else
BuildRequires:  python-module-docutils python-module-docutils-compat
%endif
BuildRequires:  autoconf-common
BuildRequires:  automake-common
BuildRequires:  libtool-common
BuildRequires:  python-module-pygobject-devel
BuildRequires:  python-module-pygtk-devel

Requires:       dropbox-uploader
Requires:       mate-file-manager-extensions
Requires:       python-module-pygtk python-module-pygtk-demo
Source44: import.info

%description
Dropbox extension for caja file manager
Dropbox allows you to sync your files online and across
your computers automatically.

%prep
%setup -n %{oldname}-%{version} -q

%build
cat > cnf <<'EOF'
#!/bin/sh
%configure
EOF
chmod 755 ./cnf
xvfb-run ./cnf


%make_build

%install
%{makeinstall_std}

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.a" -exec rm -f {} ';'

rm -rf ${RPM_BUILD_ROOT}%{_bindir}
rm -rf ${RPM_BUILD_ROOT}%{_datadir}

%files
%doc AUTHORS COPYING NEWS README 
%{_libdir}/caja/extensions-2.0/libcaja-dropbox.so


%changelog
* Fri Sep 15 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.0-alt1_2
- new fc release

* Wed Nov 02 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt1_1
- new fc release

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_1
- new version

