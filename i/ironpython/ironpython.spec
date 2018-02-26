Name: ironpython
Version: 2.6
Release: alt2

Summary: .NET Python implementation
License: Ms-PL
Group: Development/Python
Url: http://www.codeplex.com/IronPython

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar

BuildPreReq: mono-devel >= 2.6 mono-mcs mono-web
BuildPreReq: /proc

Requires: python-base

%description
IronPython is a new implementation of the Python programming language
running on .NET. It supports an interactive console with fully dynamic
compilation. It is well integrated with the rest of the .NET Framework
and makes all .NET libraries easily available to Python programmers,
while maintaining full compatibility with the Python language.


%package docs
Summary: IronPython documentation
Group: Development/Python
BuildArch: noarch

%description docs
IronPython is a new implementation of the Python programming language
running on .NET. It supports an interactive console with fully dynamic
compilation. It is well integrated with the rest of the .NET Framework
and makes all .NET libraries easily available to Python programmers,
while maintaining full compatibility with the Python language.

This package contains IronPython documentation from its distribution.


%prep
%setup
sed -i 's,Microsoft.Scripting.SilverLight\\,Microsoft.Scripting.Silverlight\\,' Src/IronPython.sln

cat > ipy << __EOF__
#!/bin/sh
exec -a ipy mono %_prefix/lib/%name/ipy.exe -X:TabCompletion -X:ColorfulConsole \$*
__EOF__


%build
xbuild Src/IronPython.sln /p:Configuration="Release" /p:TreatWarningsAsErrors=false

cat >> Bin/Release/Lib/site.py << __EOF__
import sys
sys.path.append('%python_libdir')
sys.path.append('%python_sitelibdir')
__EOF__


%install
mkdir -p %buildroot{%_prefix/lib/%name/Lib/,%_bindir/}
install -D -m755 Bin/Release/{ipy.exe,*.dll} %buildroot%_prefix/lib/%name/
rm -f %buildroot%_prefix/lib/%name/IronPythonTest.dll
install -D -m755 Bin/Release/Lib/{site.py,__future__.py} %buildroot%_prefix/lib/%name/Lib/
install -D -m755 ipy %buildroot%_bindir/


%files
%_bindir/*
%_prefix/lib/%name/
%doc License.* Readme.html Tutorial/

#%%files docs
#%%doc Tutorial/

%changelog
* Sun Mar 21 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.6-alt2
- update buildreqs

* Tue Dec 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6-alt1
- 2.6

* Tue Nov 10 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Sat Aug 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.2-alt2
- don't package ipyw.exe and IronPythonTest.dll

* Fri Aug 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.2-alt1
- 2.0.2
- fix hardcoded paths to CPython modules
- enable -X:TabCompletion -X:ColorfulConsole in the wrapper

* Sun Sep 21 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.2-alt1
- initial build
