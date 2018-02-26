Name:		yoficator
Version:	2003.07
Release:	alt1.1
Group:		Text tools
Summary:	Vim script for inserting YO instead of YE
License:	GPL
URL:		http://python.anabar.ru/yo.htm
BuildArch:	noarch

BuildPreReq:	rpm-build-vim

%setup_python_module vimtext
Requires:	%packagename

Summary(ru_RU.UTF8): Сценарий для Vim для интерактивной замены Е на Ё

Source1:	http://python.anabar.ru/macros/emin/text/text.py
Source2:	http://python.anabar.ru/macros/emin/yo/yobase.gz
Source3:	http://python.anabar.ru/macros/emin/yo/yo.py
Patch:		yo.patch

%define lexe %_prefix/libexec

%description
Vim script for inserting YO instead of YE

%description -l ru_RU.UTF8
Этот скрипт предназначен для полуавтоматической расстановки в русском
тексте буквы Ё в текстовом редакторе Vim. Слова в которых буква
Ё обязана быть, заменяются автоматически, остальные — интерактивно.

%package -n %packagename
Group: Development/Python
Summary: Python module for vim text manipulating
%description -n %packagename
Python module for vim text manipulating

# TODO start yo.py from commandline
%prep
cp %SOURCE3 .
%patch
cat > YO.vim <<@@@
" Vim plugin for calling YO-ficator script
" Maintainer: %packager
" Last Change: Thu Sep 15 12:01:18 MSK 2011

if exists('g:loaded_YOficator')
  finish
endif
let g:loaded_YOficator = 'v0.1'

" Define the :YO command when:
" - 'compatible' is not set
" - this plugin was not already loaded
" - user commands are available.
if !&cp && !exists(":YO") && has("user_commands")
  command -range=%% YO :pyfile %lexe/yo.py
endif
@@@

cat > README.alt <<@@@
Для интерактивной подставновки Е -> Ё в тексте используйте
:[range]YO
Дополнительная информация на сайте: http://python.anabar.ru/yo.htm
@@@

# TODO vim help
%build
gzip -d < %SOURCE2 > yobase.txt

%install
install -D yo.py %buildroot%lexe/yo.py
install -D yobase.txt %buildroot%_datadir/yobase.txt
install -D %SOURCE1 %buildroot%python_sitelibdir_noarch/vimtext.py
install -D YO.vim %buildroot%vim_plugin_dir/YO.vim

%files
%doc README.alt
%_prefix/libexec/yo.py
%vim_plugin_dir/YO.vim
%_datadir/yobase.txt

%files -n %packagename
%python_sitelibdir_noarch/vimtext.*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2003.07-alt1.1
- Rebuild with Python-2.7

* Thu Sep 15 2011 Fr. Br. George <george@altlinux.ru> 2003.07-alt1
- Initial build from scratch

