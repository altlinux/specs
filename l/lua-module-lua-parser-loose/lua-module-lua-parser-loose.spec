# Original package name lua-parser-loose
%define oname lua-parser-loose
%define oversion scm-1
%define rockspec lua-parser-loose-scm-1.rockspec
Name: lua-module-%oname
Version: 0.1
Release: alt4_lr1.git.g67f9007
Summary: loose parsing of Lua code, ignoring syntax errors
License: MIT/X11
Group: Development/Other
Url: https://github.com/davidm/lua-parser-loose
Provides: luarocks(%oname) = %version

BuildArch: noarch

# git://github.com/davidm/lua-parser-loose.git
Source: lua-parser-loose.tar
Source1: https://rocks.moonscript.org/manifests/luarocks/lua-parser-loose-scm-1.rockspec

BuildPreReq: rpm-macros-lua >= 1.2
# Automatically added by buildreq on ...
BuildRequires: liblua5-devel luarocks

%description
	Does loose parsing of Lua code.
	If the code has syntax errors, the parse does not abort; rather,
	some information (e.g. local and global variable scopes) is still inferred.
	This may be useful for code interactively typed into a text editor.

	Characteristics of this code:
	- Parsing does not construct any AST but rather streams tokens.
	It should be memory efficient on large files.
	It is also pretty fast.
	- Very loose parsing.
	Does not abort on broken code.
	Scopes of local variables are still resolved even if the code is
	not syntactically valid.
	- Above characteristics make it suitable for use in a text editor,
	where code may be interactively typed.
	- Loose parsing makes this code somewhat hard to validate its correctness,
	but tests are performed to verify robustness.
	- The parsing code is designed so that parts of it may be reused for other
	purposes in other projects.

%prep
%setup -n %oname

%install
%luarocks_make %SOURCE1

%check
#FIXME maybe later / needs metalua
exit 0
%lua_path_add_buildroot
for t in %buildroot%luarocks_dbdir/%oname/%oversion/test/* ; do
  lua $t
done

%files
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc COPYRIGHT* README*
%exclude %luarocks_dbdir/manifest

%changelog
* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt4_lr1.git.g67f9007
- Rebuild with new luarocks and lua-5.3

* Wed Oct 29 2014 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt3_lr1.git.g67f9007
- real new version (previous had wrong tag)

* Mon Oct 27 2014 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt2_lr1.git.g67f9007
- new version (Paul Kulchenko's fork)

* Fri Oct 17 2014 Ildar Mulyukov <ildar@altlinux.ru> 0.1-alt1_lr1.git.gf3d5901
- git HEAD (commit f3d5901bb3062a6723e17a2cb3a4baeb139419be)
