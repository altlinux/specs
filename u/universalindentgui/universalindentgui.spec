Name: universalindentgui
Version: 1.2.0
Release: alt1.1

Summary: GUI for varius source code beautifiers
License: GPL
Group: Development/Tools

Url: http://universalindent.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://prdownloads.sourceforge.net/universalindent/uigui/UniversalIndentGUI_%version/%name-%version.tar.gz
Source: %name-%version.tar
Source1: %name.desktop

Patch: %name-alt-translation.patch
Patch1: %name-alt-disabled-updates.patch

# it are examples
%add_findreq_skiplist */example.*
# due some errors
%add_findreq_skiplist */rbeautify.rb */ruby_formatter.rb

# Automatically added by buildreq on Fri Sep 06 2013
# optimized out: fontconfig libqscintilla2-8-qt4 libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-script libqt4-xml libstdc++-devel python3-base qt4-common
BuildRequires: gcc-c++ libqscintilla2-qt4-devel phonon-devel

%description
The UniversalIndentGUI is a universal graphical user
interface for source code, respective text, formatter, beautifier and
indenter. This is mainly achieved by a configuration file for each
supported indenter.

One of the main features and the reason why this tool was (better is
being right now) developed is to see how the indent parameter affects
the source code style directly while changing the parameters. It
always bothered me to change one option of a tool like GNU Indent or
GreatCode and have to run it to see what my code would look like
afterward. Often the result was not what I expected from the
parameters description. So these times are gone. Toggle a parameter
and see what it does.

%description -l ru_RU.UTF-8
UniversalIndentGUI - это универсальный графический интерфейс
к разнообразным программам, форматирующим программный код:
indent, astyle, uncrustify и д.р.

UniversalIndentGUI позволяет легко модифицировать
каждый пункт настройки любой из поддерживаемых программ
и одновременно видеть на специальном тестовом примере,
к чему это приводит.

%prep
%setup
#patch0 -p1
#patch1 -p1

%build
qmake-qt4 UniversalIndentGUI.pro
%make_build release
#lrelease-qt4 translations/*

%install
%makeinstall_std INSTALL_ROOT=%buildroot

# Маска u* для того, чтобы не копировать ненужный шлак созданный для Windows.
#install -pm644 translations/u*.qm %buildroot%_datadir/%name/translations

install -pm644 -D resources/universalIndentGUI.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
#install -pm644 -D resources/universalIndentGUI_32x32.png %buildroot%_niconsdir/%name.png
install -pm644 -D resources/universalIndentGUI_64x64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -pm644 -D %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/universalindentgui
%dir %_datadir/%name/
%_datadir/%name/config/
%_datadir/%name/indenters/
%_datadir/%name/translations/

%_man1dir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Nov 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.1
- Rebuilt with new qscintilla2

* Fri Sep 06 2013 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)
- rewrite spec, update buildreqs

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt0.7.1
- Rebuilt with python 2.6

* Sun Nov 15 2009 Andrey Bergman <vkni@altlinux.org> 1.1.0-alt0.7
- Added patch to prevent program from checking for updates
  (useless in ALT Linux environment).

* Thu Nov 12 2009 Andrey Bergman <vkni@altlinux.org> 1.1.0-alt0.5
- Changed desktop file (encoding and categories)

* Thu Oct 08 2009 Andrey Bergman <vkni@altlinux.org> 1.1.0-alt0.2
- Added translations.

* Thu Oct 08 2009 Andrey Bergman <vkni@altlinux.org> 1.1.0-0.1
- Initial release. Based on both Fedora 8 and openSuse 11
  unofficial packages.
