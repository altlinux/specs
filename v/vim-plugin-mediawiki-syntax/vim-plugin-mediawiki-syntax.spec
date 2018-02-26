Name: vim-plugin-mediawiki-syntax
Version: 0.0
Release: alt3
URL: http://en.wikipedia.org/wiki/Wikipedia:Text_editor_support#Vim
License: GPL
Group: Editors
# wget "http://en.wikipedia.org/w/index.php?title=Wikipedia:Text_editor_support&action=raw&ctype=text/css" -O Text_editor_support.wiki
Source: Text_editor_support.wiki

BuildArch: noarch

Summary: Mediawiki (Wikipedia) syntax highlighting plugin for VIM
Group: Editors
Requires: %_bindir/vim
%description
Mediawiki (Wikipedia) syntax highlighting/filetype plugin for VIM.

%prep
cat > ./cutpart <<@@@
#!/bin/sh
sed -n "/\$2/,/\$3/{
/^<syntaxhighlight/,/^<\/syntaxhighlight/p
}" "\$1" | sed '/^<syntaxhighlight/d;/^<\/syntaxhighlight/d'
@@@
chmod +x ./cutpart
cp %SOURCE0 .

%build
./cutpart %SOURCE0 \
	"syntax.Wikipedia.vim" "To autodetect files" > syntax.vim
./cutpart %SOURCE0 \
	"ftdetect.Wikipedia.vim" "articles often only have" > ftdetect.vim
./cutpart %SOURCE0 \
	"ftplugin.Wikipedia.vim" "Please feel free to contribute" > ftplugin.vim

%install
for d in syntax ftdetect ftplugin; do
  install -D $d.vim %buildroot%_datadir/vim/$d/mediawiki.vim
done

%files
%_datadir/vim/syntax/*
%_datadir/vim/ftplugin/*
%_datadir/vim/ftdetect/*
%doc *.wiki

%changelog
* Wed Jul 27 2011 Fr. Br. George <george@altlinux.ru> 0.0-alt3
- New snippet cutting scheme

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.0-alt2
- FTDetect script added

* Mon Oct 27 2008 Fr. Br. George <george@altlinux.ru> 0.0-alt1
- Initial build

