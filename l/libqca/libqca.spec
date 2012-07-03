Name:		libqca
Copyright:	GPL
Group:		Networking/Instant messaging
Summary:	QCA - Qt Cryptographic Architecture
Version:	1.0
Release:	alt4
Source:		qca-%version.tar.bz2

BuildRequires: gcc-c++ libqt3-devel libstdc++-devel

%description
This library provides an easy API for the following features: SSL/TLS,
X509, SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
    
Functionality is supplied via plugins.  This is useful for avoiding
dependence on a particular crypto library and makes upgrading easier,
as there is no need to recompile your application when adding or
upgrading a crypto plugin.  Also, by pushing crypto functionality into
plugins, your application is free of legal issues, such as export
regulation.

%description -l ru_RU.KOI8-R
Эта библиотека предоставляет простой API для следующего: SSL/TLS, X509,
SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)

Функциональность дополняется с помощью плагинов. Это удобно, так как
избегается зависимость на конкретную криптографическую библиотеку и это
делает обновления проще, так как нет необходимости перекомпилировать
использующее QCA приложение при добавлении или обновлении
крипто-плагина. Также, так как функциональность криптографии вынесена на
уровень плагинов, приложение избавляется от возможных ограничений,
накладываемых законом, например, экспортных ограничений.

%package devel
Summary: Header files for developing apps which will use Qt Crytographic Architecture (QCA)
Summary(ru_RU.KOI8-R): Файлы, необходимые для разработки приложений с использованием Qt Crytographic Architecture (QCA)
Group: Development/C++
Requires: %name = %version-%release
Requires: glibc-devel

%description devel
This library provides an easy API for the following features: SSL/TLS,
X509, SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)

This package contains the header files needed to develop programs
that use QCA.

%description devel -l ru_RU.KOI8-R
Эта библиотека предоставляет простой API для следующего: SSL/TLS, X509,
SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)

Этот пакет содержит файлы заголовков, необходимые для разработки
приложений, использующих QCA.

%prep
%setup -q -n qca-%version
%ifarch x86_64
sed -i 's|\s*target.path\s*=.*|target.path=$PREFIX/%_lib|' qcextra
%endif


%build
>conf.pri
cat >extra.pri <<__EOF__
unix: {
	# install
	target.path = %buildroot/%_libdir
	INSTALLS += target

	incfiles.path = %buildroot/%_includedir
	incfiles.files = src/qca.h
	INSTALLS += incfiles

	INSTALL_ROOT = ""
}
__EOF__

export QTDIR=%_qt3dir QMAKESPEC="default"
qmake-qt3
%make


%install
%make install INSTALL_ROOT=""

%files
%_libdir/*.so.*
%doc README INSTALL COPYING TODO

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 1.0-alt4
- fix build requires

* Mon Mar 17 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt3
- move lib*.so to devel subpackage

* Fri Jan 27 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt2.1
- fix to build on x86_64

* Sun Dec 18 2005 Mikhail Yakshin <greycat@altlinux.org> 1.0-alt2
- Fixed x86_64 build problem

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Dec 13 2004 Mikhail Yakshin <greycat@altlinux.ru> 1.0-alt1
- Initial release

