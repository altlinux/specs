%define pluginlist "chatroom forbid iplog isp messanger replacer stats"

Name: verlihub-plugins
Version: 0.1
Release: alt2.qa1

Summary: Plugins for verlihub

Url: http://www.verlihub-project.org
License: GPL
Group: Development/C

Source: http://prdownloads.sourceforge.net/verlihub/All-0.1.tar.bz2
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Automatically added by buildreq on Fri Apr 25 2008
BuildRequires: gcc-c++ libGeoIP-devel libMySQL-devel liblua5-devel libpcre-devel libverlihub-devel python-base zlib-devel

%description
This package contains various plugins for verlihub:
%pluginlist


%prep
%setup -n %name -c %name-%version

%build
for i in `echo %pluginlist` ; do
	cd $i
	%configure --disable-static
	%make_build
	cd ..
done

%install
for i in `echo %pluginlist` ; do
	cd $i
	%makeinstall_std
	cd ..
done

%files
#%doc
#%_bindir/%name
%_datadir/verlihub/*
%_libdir/*.so*
#%python_sitelibdir/*

%changelog
* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for verlihub-plugins
  * postun_ldconfig for verlihub-plugins
  * postclean-05-filetriggers for spec file

* Thu Jul 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- lua plugin build in standalone package

* Fri Apr 25 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
