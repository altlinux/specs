Name: fckeditor
Version: 2.6.5
Release: alt1.1
BuildArch: noarch

Group: Networking/WWW
Summary: The HTML text editor like MS Word.
Summary(ru_RU.UTF-8): Основанный на HTML текстовый редактор, похожий на MS Word.
Url: http://www.fckeditor.net
License: GPL
Packager: Michael A. Kangin <prividen@altlinux.org>

Source0: %name-%version.tgz

%description
FCKeditor is a lightweight text editor to be used in web pages. It provides most
of the commonly used functions from desktop editors like Word to the web. By
using FCKeditor you can write text, format it, create tables and much more. The
only thing you need to work with FCKeditor is a compatible Internet browser,
like Internet Explorer, Firefox, Safari or Opera. 


%package devel
Summary: Devel files for %name
Group: Networking/WWW
Requires: %name = %version-%release

%description devel
Sources, examples


%package php
Summary: Integration %name with PHP
Group: Networking/WWW
Requires: %name = %version-%release php-engine >= 4 aspell

%description php
%summary

%package python
Summary: Integration %name with PHP
Group: Networking/WWW
Requires: %name = %version-%release python

%description python
%summary

%package perl
Summary: Integration %name with PHP
Group: Networking/WWW
BuildPreReq: perl-CGI
Requires: %name = %version-%release perl aspell

%description perl
%summary



%prep
%setup -q

%build

%install

mkdir -p %buildroot%_datadir/%name
cp -r * %buildroot%_datadir/%name/

# Delete unused parts
cd %buildroot%_datadir/%name/
rm -rf _*.html license.txt
rm -rf fckeditor.{afp,asp,cfc,cfm,lasso} fckutils.cfm
cd editor
rm -rf fckeditor.original.html filemanager plugins/bbcode/_sample \
	lang/_translationstatus.txt skins/_fckviewstrips.html
rm -f dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.cfm

%files
%dir %_datadir/%name
%_datadir/%name/*.js
%_datadir/%name/*.xml
%_datadir/%name/editor
%exclude %_datadir/%name/editor/_source
%exclude %_datadir/%name/editor/dialog/fck_spellerpages/spellerpages/server-scripts
%doc _*.html license.txt

%files devel
%add_findreq_skiplist %_datadir/%name/_samples/py/*
%_datadir/%name/_samples
%_datadir/%name/editor/_source

%files php
%_datadir/%name/*.php
%_datadir/%name/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.php

%files python
%_datadir/%name/*.py

%files perl
%_datadir/%name/*.pl
%_datadir/%name/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.pl


%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6.5-alt1.1
- Rebuild with Python-2.7

* Thu Dec 31 2009 Michael A. Kangin <prividen@altlinux.org> 2.6.5-alt1
- New version 

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4.1-alt1.1
- Rebuilt with python 2.6

* Sat Jul 25 2009 Michael A. Kangin <prividen@altlinux.org> 2.6.4.1-alt1
- Initial release



