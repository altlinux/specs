# -*- coding: utf-8 -*-
# vim: enc=utf-8

%define version 1.2
%define release alt5
%setup_python_module id3-py

Name: %{packagename}
Version: %{version}
Release: %{release}.1
Packager: Python Development Team <python at packages.altlinux.org>
Summary: ID3 tags Python module
Summary(ru_RU.UTF-8): Модуль для работы с ID3-тэгами на python
License: GPL
Group: Development/Python
Url: http://id3-py.sourceforge.net
BuildArch: noarch
Source: http://prdownloads.sourceforge.net/%modulename/%{modulename}_%version.tar.gz
Prefix: %{_prefix}

# Automatically added by buildreq on Fri Jun 25 2004
BuildRequires: python-devel python-modules-encodings

Provides: id3-py = %version-%release
Obsoletes: id3-py <= 1.2-alt1

%description
id3-py is a simple Python module for retrieving and setting so-called
ID3 tags on MP3 compressed audio files through an object-oriented
interface. MP3 players generally use this simple information for
display track title, artist name, and album title while playing
the sound file.

ID3.py supports ID3 version 1.1, including the track number field.

This module is built for python %__python_version


%description -l ru_RU.UTF-8

id3-py - простое расширение языка Python для чтения и записи информации
ID3-тэгов аудио-файлов формата MP3 с обьектно-ориентированным
интерфейсом. MP3-плейеры обычно используют эту информацию для показа
названия песни, альбома и имени исполнителя во время воспроизведения
звукового файла.

ID3.py поддерживает ID3 версии 1.1, включая поле номера трека.

Этот модуль собран для Python версии %__python_version


%prep
%setup -q -n %modulename-%version

%build
env CFLAGS="$RPM_OPT_FLAGS" %__python setup.py build

%install
%__python setup.py install --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc CHANGES README id3-tagger.py

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt5.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt5
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.2-alt4.1
- Rebuilt with python-2.5.

* Sat Mar 12 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.2-alt4
- Rebuild with python 2.4

* Wed Oct 13 2004 Eugene Vlasov <eugvv@altlinux.ru> 1.2-alt3
- Renamed spec file

* Sun Jun 27 2004 Eugene Vlasov <eugvv@altlinux.ru> 1.2-alt2
- Fix new python policy compatibility
- Other minor spec changes

* Thu Dec 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2-alt1
- First build for Sisyphus.

