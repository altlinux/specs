Name: freedink-data
Version: 1.08.20100103
Release: alt1
Summary: Adventure and role-playing game (game data)

Group: Games/Adventure
License: zlib and CC-BY-SA and (GPLv3+ or Free Art or CC-BY-SA) and OAL and Public Domain and CC-BY and GPLv2+
Url: http://www.freedink.org/
Source: ftp://ftp.gnu.org/gnu/freedink/%name-%version.tar.gz
#Source0:	http://www.freedink.org/releases/%name-%version.tar.gz
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

%description
Dink Smallwood is an adventure/role-playing game, similar to Zelda,
made by RTsoft. Besides twisted humour, it includes the actual game
editor, allowing players to create hundreds of new adventures called
Dink Modules or D-Mods for short.

This package contains architecture-independent data for the original
game, along with free sound and music replacements.

%prep
%setup -q
# Strip DOS EOL from documentation
# https://fedoraproject.org/wiki/PackageMaintainers/Common_Rpmlint_Issues#wrong-file-end-of-line-encoding
sed -i 's/\r//' README.txt README-REPLACEMENTS.txt

%build
%install
make install PREFIX=%prefix DESTDIR=$RPM_BUILD_ROOT

%files
%doc README.txt README-REPLACEMENTS.txt licenses/
%_datadir/dink/

%changelog
* Mon May 24 2010 Fr. Br. George <george@altlinux.ru> 1.08.20100103-alt1
- Version up

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 1.08.20090706-alt1
- Initial build from FC

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20090706-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090706-1
- New upstream release (remove savegame)

* Sun Jul 05 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090705-1
- New upstream release
- Removed patch to preserve timestamps (applied upstream)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20080920-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-3
- Actually apply patch0 (preserve timestamps)

* Tue Sep 23 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-2
- Specify all licenses used by the package
- Added licenses texts in docs
- Replaced /usr by a RPM macro
- Add patch from upstream to preserve timestamps no install
- Converted DOS newlines

* Sat Sep 20 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-1
- Initial package
