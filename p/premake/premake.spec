Name: premake
Version: 4.3
Release: alt1
Summary: Cross-platform build configuration tool

Group: Development/Tools
License: BSD
Url: http://industriousone.com/premake
Source0: http://downloads.sourceforge.net/%name/premake-%version-src.zip
# This patch removes the bundeled Lua sources from the makefile to use the system Lua
Patch0: premake-4.3-system-lua.patch
# Add the missing manpage
Patch1: premake-4.3-manpage.patch

#BuildRequires: lua-devel readline-devel

# Automatically added by buildreq on Sat Jun 11 2011
BuildRequires: liblua5-devel libreadline-devel unzip

%description
Premake is a build configuration tool that can generate project files for:
 - GNU make
 - Code::Blocks
 - CodeLite
 - MonoDevelop
 - SharpDevelop
 - Apple XCode
 - Microsoft Visual Studio

%prep
%setup
%patch0 -p0
%patch1 -p0
# Inject optflags into CFLAGS
sed -i "s/^\s*CFLAGS\s*+=.*/CFLAGS += \$(CPPFLAGS) %optflags/" build/gmake.unix/Premake4.make
# Disable stripping the executable
sed -i "s/^\s*LDFLAGS\s*+= -s/LDFLAGS +=/" build/gmake.unix/Premake4.make
# Use the release build for running tests
sed -i "s/debug/release/" tests/test

%build
cd build/gmake.unix/
make verbose=true %{?_smp_mflags}

%install
rm -rf %buildroot
install -m 755 -Dp ./bin/release/premake4 %buildroot/%_bindir/premake4
install -m 644 -Dp ./premake4.1 %buildroot/%_mandir/man1/premake4.1

%clean
rm -rf %buildroot

%files
%_bindir/premake4
%_mandir/man1/premake4.1*
%doc LICENSE.txt README.txt CHANGES.txt

%changelog
* Sat Jun 11 2011 Fr. Br. George <george@altlinux.ru> 4.3-alt1
- Initial build from FC

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 28 2010 Joachim de Groot <jdegroot@web.de> - 4.3-2
- Let rpm handle the man page compression

* Sat Nov 27 2010 Joachim de Groot <jdegroot@web.de> - 4.3-1
- Update to 4.3, thus changed license to BSD
- Added missing version numbers to changelog
- Added readline-devel to BuildRequires
- Added a man page

* Fri Oct 29 2010 Joachim de Groot <jdegroot@web.de> - 4.2.1-3
- Correct building of the debuginfo package

* Fri Oct 29 2010 Joachim de Groot <jdegroot@web.de> - 4.2.1-2
- Implemented changes proposed by Mohamed El Morabity

* Thu Oct 28 2010 Joachim de Groot <jdegroot@web.de> - 4.2.1-1
- Initial version of the package

