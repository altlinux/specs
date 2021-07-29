%define mname texamator
Name: TeXamator
Version: 3.0
Release: alt0.1

Summary: Helping you making your exercise sheets
License: GPL-3.0
Group: Other
Url: http://snouffy.free.fr/blog-en/index.php/category/TeXamator
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildArch: noarch

Source0: http://snouffy.free.fr/blog-en/public/TeXamator/%name.v.%version.tar.gz
Source1: %name.desktop
Source44: import.info

BuildRequires(pre): rpm-build-python3
BuildRequires: desktop-file-utils python3-tools

Requires: /usr/bin/latex texlive-latex-recommended
Requires: dvipng

%add_python3_req_skip partielatormods
%filter_from_requires /^python2.*/d


%description
TeXamator is written in Python/Qt4. It is aimed at helping you making your
exercise sheets. Basically, it browses a specified directory, looks for .tex
files containing exercises and builds a tree with all your exercises in it. You
can click on an element of the tree to have a preview of the exercise and add
it to a list if you wish to. Then you can save your work to a .tex file or you
can generate a .dvi file.

%prep
%setup -n %name
find -name '*~' -delete # Remove backup file in source package

$(find /usr/lib*/python%{_python3_version}/Tools/scripts/reindent.py) \
                                              $(find ./ -name '*.py')

%build
%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name
cp -rp partielatormods %buildroot%_datadir/%name
cp -rp ts_files %buildroot%_datadir/%name
cp -rp ui_files %buildroot%_datadir/%name
cp -p %mname.py %buildroot%_datadir/%name/%name.py
ln -sr %_datadir/%name/%name.py %buildroot%_bindir/%name # Create a link in _bindir
# Remove shebang from Python libraries
sed -i -e '/\/usr\/bin\/python/d' %buildroot%_datadir/%name/partielatormods/*.py
for lib in %buildroot%_datadir/%name/partielatormods/*/*.py; do
 sed '/\/usr\/bin\/python/d' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
# Remove developer's utility not need by the application
rm -f %buildroot%_datadir/%name/ui_files/plop.sh
# Add .desktop file
desktop-file-install --dir=%buildroot%_datadir/applications %SOURCE1
desktop-file-validate %buildroot/%_datadir/applications/%name.desktop

%files
%doc README* gpl-3.0.txt
%_bindir/%name
%_datadir/%name
%_datadir/applications/%name.desktop


%changelog
* Thu Jul 29 2021 Sergey V Turchin <zerg@altlinux.org> 3.0-alt0.1
- 3.0+git.20190226.91432e4

* Fri Mar 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.7.5-alt3
- Porting to python3.

* Sat Mar 01 2014 Ilya Mashkin <oddity@altlinux.ru> 1.7.5-alt2
- Build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.5-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.5-alt1_2
- initial fc import

