Name: faust
Version: 0.9.9.4
Release: alt2

Summary: FAUST is a compiled language for real-time audio signal processing
License: GPL
Group: Sound
Url: http://faust.grame.fr/

Packager: Timur Batyrshin <erthad@altlinux.org>
Source: %name-%version.tar.bz2
#Patch: %name-1.0-alt-makefile-fixes.patch

BuildRequires(pre): gcc-c++

%description
FAUST is a compiled language for real-time audio signal processing.

The name FAUST stands for Functional AUdio STream. Its programming model 
combines two approaches : functional programming and block diagram composition.
You can think of FAUST as a structured block diagram language with a textual syntax.

Programming with FAUST is somehow like working with electronic circuits
and signals. A FAUST program is a list of definitions that defines a signal
processor block-diagram : a piece of code that produces output signals
according to its input signals (and maybe some user interface parameters).

Faust is a compiled language translated to C++. In order to generate the most
efficient code, the compilation is based on a semantic approach. Instead of
compiling directly the block-diagram as described by the user, the idea is to
compile its mathematical meaning (what it actually computes). 


%package doc
Summary: Documentation for FAUST, a compiled language for real-time audio signal processing
Group: Sound
BuildArch: noarch

%description doc
FAUST is a compiled language for real-time audio signal processing.

The name FAUST stands for Functional AUdio STream. Its programming model 
combines two approaches : functional programming and block diagram composition.
You can think of FAUST as a structured block diagram language with a textual syntax.

Programming with FAUST is somehow like working with electronic circuits
and signals. A FAUST program is a list of definitions that defines a signal
processor block-diagram : a piece of code that produces output signals
according to its input signals (and maybe some user interface parameters).

Faust is a compiled language translated to C++. In order to generate the most
efficient code, the compilation is based on a semantic approach. Instead of
compiling directly the block-diagram as described by the user, the idea is to
compile its mathematical meaning (what it actually computes). 

This package contains documentation for FAUST


%package -n faust2appls
Summary: Useful scripts that combines faust and g++ to generates executable binary
Group: Sound
Requires: %name

%description -n faust2appls
FAUST is a compiled language for real-time audio signal processing.

The name FAUST stands for Functional AUdio STream. Its programming model 
combines two approaches : functional programming and block diagram composition.
You can think of FAUST as a structured block diagram language with a textual syntax.

Programming with FAUST is somehow like working with electronic circuits
and signals. A FAUST program is a list of definitions that defines a signal
processor block-diagram : a piece of code that produces output signals
according to its input signals (and maybe some user interface parameters).

Faust is a compiled language translated to C++. In order to generate the most
efficient code, the compilation is based on a semantic approach. Instead of
compiling directly the block-diagram as described by the user, the idea is to
compile its mathematical meaning (what it actually computes). 

This package contains some useful scripts for FAUST


%prep
%setup
#patch -p1

%build
#configure
%make_build

%install
mkdir -p %buildroot/%_bindir/
%makeinstall install
%find_lang %name

mkdir -p %buildroot/%_docdir/%name-%version/
cp -ar README COPYING documentation/*.pdf %buildroot%_docdir/%name-%version/
install -pD -m0644 documentation/additional\ documentation %buildroot%_docdir/%name-%version/additional_documentation
cp -ar examples/ %buildroot%_docdir/%name-%version/
install -pD -m0644 tools/README %buildroot%_docdir/%name-%version/README.tools

pushd tools/faust2appls
%makeinstall install
install -pD -m0644 README %buildroot%_docdir/%name-%version/README.faust2appls
popd

%files -f %name.lang
%dir %doc %_docdir/%name-%version/
%doc %_docdir/%name-%version/README
%doc %_docdir/%name-%version/COPYING
%doc %_docdir/%name-%version/README.tools
%_bindir/%name
%_datadir/%name/

%files doc
%doc %_docdir/%name-%version/*.pdf
%doc %_docdir/%name-%version/additional_documentation

%files -n faust2appls
%_bindir/faust2*
%doc %_docdir/%name-%version/README.faust2appls

%changelog
* Fri Jul 31 2009 Timur Batyrshin <erthad@altlinux.org> 0.9.9.4-alt2
- minor gcc fixes

* Fri Jul 31 2009 Timur Batyrshin <erthad@altlinux.org> 0.9.9.4-alt1
- package name fix

* Sun Apr 26 2009 Timur Batyrshin <erthad@altlinux.org> 0.9.9.4-alt0.2
- appls and docs added

* Thu Apr 23 2009 Timur Batyrshin <erthad@altlinux.org> 0.9.9.4-alt0.1
- initial build
