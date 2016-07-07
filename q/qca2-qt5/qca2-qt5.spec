Name: qca2-qt5
%define major 2
%define minor 1
%define bugfix 1
Version: %major.%minor.%bugfix
Release: alt2

Group: Networking/Instant messaging
Summary: QCA - Qt Cryptographic Architecture
License: LGPL
Url: https://github.com/KDE/qca

#VCS: https://github.com/KDE/qca.git
Source: qca-%version.tar
# ALT
Patch10: qca-2.0.3-alt-paths.patch

Requires: lib%name = %version-%release
Requires: ca-certificates

BuildRequires: cmake gcc-c++ qt5-base-devel ca-certificates
BuildRequires: libgcrypt-devel libnss-devel  libsasl2-devel pkcs11-helper-devel

%package -n lib%name
Summary: QCA - Qt Cryptographic Architecture library
Summary(ru_RU.UTF-8): Файлы, необходимые для разработки приложений с использованием Qt Crytographic Architecture (QCA)
Group: System/Libraries
Requires: ca-certificates

%package -n lib%name-devel
Summary: Header files for developing apps which will use Qt Crytographic Architecture (QCA)
Summary(ru_RU.UTF-8): Файлы, необходимые для разработки приложений с использованием Qt Crytographic Architecture (QCA)
Group: Development/KDE and QT
Requires: lib%name = %version-%release

%description
  This library provides an easy API for the following features: SSL/TLS,
X509, SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Functionality is supplied via plugins.  This is useful for avoiding
dependence on a particular crypto library and makes upgrading easier,
as there is no need to recompile your application when adding or
upgrading a crypto plugin.  Also, by pushing crypto functionality into
plugins, your application is free of legal issues, such as export
regulation.
%description -l ru_RU.UTF-8
  Эта библиотека предоставляет простой API для следующего: SSL/TLS, X509,
SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Функциональность дополняется с помощью плагинов. Это удобно, так как
избегается зависимость на конкретную криптографическую библиотеку и это
делает обновления проще, так как нет необходимости перекомпилировать
использующее QCA приложение при добавлении или обновлении
крипто-плагина. Также, так как функциональность криптографии вынесена на
уровень плагинов, приложение избавляется от возможных ограничений,
накладываемых законом, например, экспортных ограничений.

%description -n lib%name
  This library provides an easy API for the following features: SSL/TLS,
X509, SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Functionality is supplied via plugins.  This is useful for avoiding
dependence on a particular crypto library and makes upgrading easier,
as there is no need to recompile your application when adding or
upgrading a crypto plugin.  Also, by pushing crypto functionality into
plugins, your application is free of legal issues, such as export
regulation.
%description -n lib%name -l ru_RU.UTF-8
  Эта библиотека предоставляет простой API для следующего: SSL/TLS, X509,
SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Функциональность дополняется с помощью плагинов. Это удобно, так как
избегается зависимость на конкретную криптографическую библиотеку и это
делает обновления проще, так как нет необходимости перекомпилировать
использующее QCA приложение при добавлении или обновлении
крипто-плагина. Также, так как функциональность криптографии вынесена на
уровень плагинов, приложение избавляется от возможных ограничений,
накладываемых законом, например, экспортных ограничений.
%description -n lib%name-devel
This package contains the header files needed to develop programs
that use QCA.
%description -n lib%name-devel -l ru_RU.UTF-8
Этот пакет содержит файлы заголовков, необходимые для разработки
приложений, использующих QCA.

%package ossl
Group: System/Libraries
Summary: QCA SSL Plugin
%description ossl
This is a plugin to provide SSL capability to programs that
utilize the Qt Cryptographic Architecture (QCA)
* Hashing - SHA1, SHA0, RIPEMD160, MD2, MD4, MD5
* Hashing - SHA224, SHA256, SHA384 and SHA512 (for openssl 0.9.8)
* Block Ciphers
* Keyed Hash Message Authentication Code (HMAC), using SHA1, MD5, RIPEMD160
* Public keys - RSA, DSA, Diffie-Hellman
* PKCS#12
* SSL/TLS
* CMS (for S/MIME)
%description ossl -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования SSL для
программ, поддерживающих Qt Cryptographic Architecture (QCA)
* Hashing - SHA1, SHA0, RIPEMD160, MD2, MD4, MD5
* Hashing - SHA224, SHA256, SHA384 and SHA512 (for openssl 0.9.8)
* Block Ciphers
* Keyed Hash Message Authentication Code (HMAC), using SHA1, MD5, RIPEMD160
* Public keys - RSA, DSA, Diffie-Hellman
* PKCS#12
* SSL/TLS
* CMS (for S/MIME)

%package cyrus-sasl
Group: System/Libraries
Summary: QCA SASL Plugin
%description cyrus-sasl
This is a plugin to provide SASL capability to programs that
utilize the Qt Cryptographic Architecture (QCA).
%description cyrus-sasl -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования SASL для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package gnupg
Group: System/Libraries
Summary: QCA GnuPG Plugin
%description gnupg
This is a plugin to provide GnuPG capability to programs that
utilize the Qt Cryptographic Architecture (QCA).
%description gnupg -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования GnuPG для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package nss
Group: System/Libraries
Summary: QCA NSS Plugin
%description nss
This is a plugin to provide Mozilla NSS capability to programs that
utilize the Qt Cryptographic Architecture (QCA)
* Hashing
%description nss -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования Mozilla NSS для
программ, поддерживающих Qt Cryptographic Architecture (QCA)
* Хеширование

%package gcrypt
Group: System/Libraries
Summary: QCA GCrypt Plugin
%description gcrypt
This plugin provides features based on libgcrypt to programs that
utilize the Qt Cryptographic Architecture (QCA)
* Hashing - SHA1, SHA256, SHA384, SHA512
* Symmetric encryption - AES128
%description gcrypt -l ru_RU.UTF-8
Этот плагин предоставляет функциональность libgcrypt для
программ, поддерживающих Qt Cryptographic Architecture (QCA)
* Хеширование - SHA1, SHA256, SHA384, SHA512
* Симметричное шифрование - AES128

%package pkcs11
Group: System/Libraries
Summary: QCA pkcs11 smartcard integration
%description pkcs11
This plugin supports the following features:
 - Multiple providers
 - Multiple tokens
 - Private key signature and decryption
 - Keystore objects serialization
 - Keystore update notifications
 - Asker integration for token and PIN

%package logger
Group: System/Libraries
Summary: QCA Logger Plugin
%description logger
Provides simple logger writer to programs that
utilize the Qt Cryptographic Architecture (QCA).
%description logger -l ru_RU.UTF-8
Этот плагин предоставляет возможность записи журналов для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package softstore
Group: System/Libraries
Summary: QCA Logger Plugin
%description softstore
Provides simple persistent certificate store to programs that
utilize the for Qt Cryptographic Architecture (QCA).
%description softstore -l ru_RU.UTF-8
Этот плагин предоставляет хранилище сертификатов для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%prep
%setup -q -n qca-%version
%patch10 -p1

%build
export QC_CERTSTORE_PATH="%_datadir/ca-certificates/ca-bundle.crt"
%cmake \
    -DBUILD_TESTS=OFF \
    -DQCA_INSTALL_IN_QT_PREFIX=OFF \
    -Dqca_CERTSTORE=%_datadir/ca-certificates/ca-bundle.crt \
    -DQCA_GPG_EXECUTABLE=gpg \
    -DQT5_BUILD=ON \
    -DQCA_PLUGINS_INSTALL_DIR:STRING=%_qt5_plugindir \
    -DQCA_FEATURE_INSTALL_DIR:STRING=%_qt5_prefix/mkspecs/features
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/mozcerts-qt5
%_bindir/qcatool-qt5
%_man1dir/*

%files -n lib%name
%_libdir/libqca-qt5.so.*
%doc README INSTALL TODO

%files logger
%_qt5_plugindir/crypto/libqca-logger.so
%files softstore
%_qt5_plugindir/crypto/libqca-softstore.so
%files ossl
%_qt5_plugindir/crypto/libqca-ossl.so
%files cyrus-sasl
%_qt5_plugindir/crypto/libqca-cyrus-sasl.so
%files gnupg
%_qt5_plugindir/crypto/libqca-gnupg.so
%files gcrypt
%_qt5_plugindir/crypto/libqca-gcrypt.so
%files nss
%_qt5_plugindir/crypto/libqca-nss.so
%files pkcs11
%_qt5_plugindir/crypto/libqca-pkcs11.so

%files -n lib%name-devel
%_libdir/libqca-qt5.so
%_pkgconfigdir/qca2-qt5.pc
%_libdir/cmake/Qca-qt5/
%_datadir/qt5/mkspecs/features/crypto.prf
%_includedir/Qca-qt5/

%changelog
* Thu Jul 07 2016 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt2
- updated to v2.1.1-17-geb5eeca
- build against Qt5 libraries

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Thu Jun 25 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.0.3-alt2
- rebuild with new libgcrypt

* Wed May 27 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.0.3-alt1
- new version

* Wed Oct 30 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt5
- rebuilt with new libsasl2

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt4
- fix against gcc-4.7

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt2.M60P.1
- built for M60P

* Tue Jul 24 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt3
- built pkcs11 plugin

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt2
- fix build requires

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt1
- new version
- sources taken from kde svn

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt2
- rebuilt with new ssl

* Fri Jun 26 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt0.M50.1
- build for M50

* Fri Jun 26 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version

* Tue Mar 31 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1.M50.1
- built for M50

* Tue Mar 31 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt2
- fix to work QT_CONFIG += crypto

* Wed Aug 06 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.1-alt1
- new version

* Wed Mar 19 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.0-alt2
- fix pkgconfig file

* Tue Mar 18 2008 Sergey V Turchin <zerg at altlinux dot org> 2.0.0-alt1
- initial specfile
