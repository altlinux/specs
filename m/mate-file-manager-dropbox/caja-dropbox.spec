# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pkg-config /usr/bin/python /usr/bin/rst2man pkgconfig(glib-2.0) pkgconfig(libcaja-extension)
# END SourceDeps(oneline)
BuildRequires: xvfb-run
BuildRequires: mate-common
%define _libexecdir %_prefix/libexec
%define oldname caja-dropbox
# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.12

Summary: 		Dropbox extension for caja
Name: 			mate-file-manager-dropbox
Version: 		1.12.0
Release: 		alt1_1
License: 		GPLv2+
Group: 			Graphical desktop/MATE
URL: 			http://git.mate-desktop.org/%{oldname}
Source0: 		http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz

ExclusiveArch:  i686 x86_64

BuildRequires:  mate-file-manager-devel
BuildRequires:  python-module-docutils
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  python-module-pygobject-devel
BuildRequires:  python-module-pygtk-devel

Requires:       dropbox-uploader 
Requires:       mate-file-manager-extensions
Requires:       pygtk2
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


make %{?_smp_mflags}

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
* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_1
- new version

