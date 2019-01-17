Name: wordlist
Version: 20180416
Release: alt1

Summary: Spell Checker Oriented Word Lists
# The only LGPL-2.1-only part is scowl/speller/aspell/en_phonet.dat
License: MIT and BSD-3-Clause and LGPL-2.1-only
Group: Text tools
Url: http://wordlist.aspell.net

# This is correct as long as we do not build aspell-en.
BuildArch: noarch

# https://github.com/en-wl/wordlist
# git://git.altlinux.org/gears/w/wordlist
Source: %name-%version-%release.tar

BuildRequires: aspell dos2unix gcc-c++ vim-console vim-spell-source unzip zip

%description
SCOWL (Spell Checker Oriented Word Lists) is a database of English words that
can be used to create word lists suitable for use in spell checkers of various
sizes and dialects (US, British, Canadian and Australian).
However, the author is sure it will have numerous other uses as well.

%package common
Summary: Spell Checker Oriented Word Lists common files
License: MIT
Group: Text tools

%description common
This package contains files common among all dictionaries generated from
the SCOWL (Spell Checker Oriented Word Lists) database of English words.

%package -n vim-spell-en
Summary: English spelling dictionaries for VIM
License: MIT and BSD-3-Clause
Group: Text tools
Requires: %name-common = %EVR

%description -n vim-spell-en
This package contains English spelling dictionaries for VIM generated from
the SCOWL (Spell Checker Oriented Word Lists) database of English words.

%package -n hunspell-en
Summary: English hunspell dictionaries
License: MIT and BSD-3-Clause
Group: Text tools
Requires: hunspell-en_AU = %EVR
Requires: hunspell-en_CA = %EVR
Requires: hunspell-en_GB = %EVR
Requires: hunspell-en_US = %EVR

%description -n hunspell-en
This package pulls in all English hunspell dictionaries.

%package -n hunspell-en_AU
Summary: Australian English hunspell dictionary
License: MIT and BSD-3-Clause
Group: Text tools
Requires: %name-common = %EVR

%description -n hunspell-en_AU
This package contains an Australian English hunspell dictionary generated
from the SCOWL (Spell Checker Oriented Word Lists) database of English words.

%package -n hunspell-en_CA
Summary: Canadian English hunspell dictionary
License: MIT and BSD-3-Clause
Group: Text tools
Requires: %name-common = %EVR

%description -n hunspell-en_CA
This package contains a Canadian English hunspell dictionary generated from
the SCOWL (Spell Checker Oriented Word Lists) database of English words.

%package -n hunspell-en_GB
Summary: British English hunspell dictionaries
License: MIT and BSD-3-Clause
Group: Text tools
Requires: %name-common = %EVR

%description -n hunspell-en_GB
This package contains a British English hunspell dictionaries (both -ise and
-ize) generated from the SCOWL (Spell Checker Oriented Word Lists) database
of English words.

%package -n hunspell-en_US
Summary: US English hunspell dictionary
License: MIT and BSD-3-Clause
Group: Text tools
Requires: %name-common = %EVR

%description -n hunspell-en_US
This package contains a US English hunspell dictionary generated from
the SCOWL (Spell Checker Oriented Word Lists) database of English words.

%prep
%setup -n %name-%version-%release
echo %version > scowl/VERSION

%build
make CXXFLAGS="$RPM_OPT_FLAGS"
make -C scowl/speller hunspell

mkdir vim
cp -p scowl/speller/en_{US,CA,GB}.{aff,dic} vim/
cd vim
# This does not include en_AU yet because en_AU.diff does not apply.
%define vim_langs en_US en_CA en_GB
for lang in %vim_langs; do
	# UTF8 substitution is for all *.diff files,
	# the dirty hack is for en_GB.diff only.
	sed -r 's/UTF8/UTF-8/;/^\*{3} (9325,9327|22885,22887) \*{4}$/,/^\*{15}$/d' \
		< %vim_spell_source_dir/en/$lang.diff |
	patch
done
%mkvimspell -a                 en %vim_langs
%mkvimspell -L en_US.ISO8859-1 en %vim_langs
%mkvimspell -L en_US.UTF-8     en %vim_langs
cd -

%install
mkdir -p %buildroot%_datadir/myspell
install -pm644 scowl/speller/en_{AU,CA,GB,US}.{aff,dic} \
	%buildroot%_datadir/myspell/

%define docdir %_docdir/%name
mkdir -p %buildroot%docdir
install -pm644 scowl/speller/hunspell/README \
	%buildroot%docdir/

mkdir -p %buildroot%vim_spell_dir
install -pm644 vim/en.* %buildroot%vim_spell_dir/

for lang in AU CA GB US; do
	ln -s %name %buildroot%_docdir/hunspell-en_$lang
done
ln -s %name %buildroot%_docdir/vim-spell-en

%define _unpackaged_files_terminate_build 1

%files common
%dir %docdir/
%docdir/README

%files -n vim-spell-en
%_docdir/vim-spell-en
%vim_spell_dir/en.*

%files -n hunspell-en

%files -n hunspell-en_AU
%_docdir/hunspell-en_AU
%_datadir/myspell/en_AU.*

%files -n hunspell-en_CA
%_docdir/hunspell-en_CA
%_datadir/myspell/en_CA.*

%files -n hunspell-en_GB
%_docdir/hunspell-en_GB
%_datadir/myspell/en_GB.*

%files -n hunspell-en_US
%_docdir/hunspell-en_US
%_datadir/myspell/en_US.*

%changelog
* Thu Jan 17 2019 Dmitry V. Levin <ldv@altlinux.org> 20180416-alt1
- Generated vim-spell-en and hunspell-en packages from the SCOWL
  (Spell Checker Oriented Word Lists) database of English words.
