%define Name OpenTK
Name: opentk
Version: 1.1
Release: alt1.rc2
Summary: C# library that wraps OpenGL, OpenCL and OpenAL
License: MIT and BSD
URL: http://www.opentk.com/
Group: Development/Other
Source: %name-%version.tar
BuildRequires: mono-devel mono-winforms
BuildRequires: dos2unix
BuildRequires: /proc

%description
The Open Toolkit is an advanced, low-level C# library that wraps OpenGL, OpenCL
and OpenAL. It is suitable for games, scientific applications and any other
project that requires 3d graphics, audio or compute functionality.

%package doc
Requires: %name = %version-%release
Summary: Documentation for %name
Group: Development/Other
BuildArch: noarch

%description doc
The Open Toolkit is an advanced, low-level C# library that wraps OpenGL, OpenCL
and OpenAL. It is suitable for games, scientific applications and any other
project that requires 3d graphics, audio or compute functionality.

This package contains the manual and several examples.

%prep
%setup -q

for file in Documentation/License.txt Source/Examples/Data/Shaders/Parallax_FS.glsl; do
  iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
done

# Shouldn't harm the correct ones
find Source/Examples -type f -exec dos2unix {} \;
echo '/* Nothing here */' >> Source/Examples/OpenGLES/SimpleWindow20.cs

%build
export LANG=en_US.UTF-8
xbuild %Name.sln /p:Configuration=Release || xbuild %Name.sln /p:Configuration=Release
chmod -x Source/Examples/obj/Release/Examples.exe

%install
mkdir -p %buildroot%_monogacdir
gacutil -i Binaries/OpenTK/Release/%Name.dll -f -package %Name -root %buildroot%_prefix/lib
gacutil -i Binaries/OpenTK/Release/%Name.Compatibility.dll -f -package %Name -root %buildroot%_prefix/lib
gacutil -i Binaries/OpenTK/Release/%Name.GLControl.dll -f -package %Name -root %buildroot/%_prefix/lib

%files
%doc Documentation/*.txt
%_monogacdir/%{Name}*
%_monodir/%Name

%files doc
%doc Documentation/Manual.pdf
%doc Source/Examples

%changelog
* Wed Feb 12 2014 Dmitry Derjavin <dd@altlinux.org> 1.1-alt1.rc2
- Initial ALTLinux build.
