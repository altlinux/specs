Summary:        Parsing Expression Grammars for Lua
Name:           lua5-lpeg
Version:        0.12
Release:        alt1
URL:            http://www.inf.puc-rio.br/~roberto/lpeg/
Packager: 	Valentin Rosavitskiy <valintinr@altlinux.org>
License:        MIT
Group: 		Development/Other

BuildRequires:  liblua5-devel lua5
Source0:        %name-%version.tar

%description
LPeg is a new pattern-matching library for Lua, based on Parsing
Expression Grammars (PEGs).

%prep
%setup -q

%build
make %_smp_mflags COPT="%optflags"

%install
mkdir -p %buildroot%_libdir/lua5
install -p -m644 lpeg.so %buildroot%_libdir/lua5/lpeg.so

mkdir -p %buildroot%_datadir/lua5
install -p -m644 re.lua %buildroot%_datadir/lua5

%files
%doc HISTORY lpeg.html re.html lpeg-128.gif test.lua
%_libdir/lua5/lpeg.so
%_datadir/lua5/*

%changelog
* Thu Jul 10 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.12-alt1
- Initial build

