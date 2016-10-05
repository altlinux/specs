Group: Development/Other
%global luaver 5.3
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:		lua-markdown
Version:	0.32
Release:	alt1_8
BuildArch:	noarch
Summary:	Markdown module for Lua
License:	MIT
URL:		http://www.frykholm.se/files/markdown.lua
Source0:	http://www.frykholm.se/files/markdown.lua
Source1:	http://www.frykholm.se/files/markdown-tests.lua
Patch0:		lua-markdown-0.32-lua-5.2.patch
BuildRequires:	lua >= %{luaver}
Requires:	lua >= %{luaver}
Source44: import.info

%description
This is an implementation of the popular text markup language Markdown
in pure Lua.  Markdown can convert documents written in a simple and
easy to read text format to well-formatted HTML.


%prep
%setup -c -T
cp -av %{SOURCE0} .
cp -av %{SOURCE1} .
%patch0 -p1 -b .lua-52


%build
# nothing to do here


%install
mkdir -p %{buildroot}%{luapkgdir}
mkdir -p %{buildroot}%{_bindir}
cp -av markdown.lua %{buildroot}%{luapkgdir}

# fix script
sed -i %{buildroot}%{luapkgdir}/markdown.lua -e '1{/^#!/d}'

# create a wrapper
echo -en '#!/bin/sh\nlua %{luapkgdir}/markdown.lua "$@"' \
  > %{buildroot}%{_bindir}/markdown.lua
chmod +x %{buildroot}%{_bindir}/markdown.lua


%check
lua markdown.lua -t


%files
%{_bindir}/markdown.lua
%{luapkgdir}/markdown.lua


%changelog
* Wed Oct 05 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.32-alt1_8
- converted for ALT Linux by srpmconvert tools

