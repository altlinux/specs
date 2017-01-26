# SPEC file for password-store package

Name:    password-store
Version: 1.6.5
Release: alt1

Summary: a simple password manager using standard Unix tools
Summary(ru_RU.UTF-8): простой и использующий стандартные средства менеджер паролей

License: %gpl2plus
Group:   Text tools
URL:     https://www.passwordstore.org/
#URL:    http://zx2c4.com/projects/password-store/
#URL:    http://git.zx2c4.com/password-store/

BuildArch: noarch

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-alt-1.6.5-shebang.patch
Patch2:  %name-alt-1.6.5-dirtree.patch

BuildRequires(pre): rpm-build-licenses rpm-build-vim

# Automatically added by buildreq on Wed Jan 25 2017
# optimized out: libgpg-error python-base python-modules python3 tzdata
BuildRequires: dirtree git-core gnupg gnupg2 pwgen

#Requires: xclip gnupg2 /usr/bin/qdbus

%description
A simple console password manager that follows Unix philosophy.
With pass, each password lives inside of a GnuPG encrypted text
file whose filename is the title of the website or resource
that requires the password. These encrypted files may be
organized into meaningful folder hierarchies, copied from
computer to computer, and, in general, manipulated using
standard command line file management utilities.

Multiple GPG keys can be specified, for using pass in a team
setting, and different folders can have different GPG keys.
Password changes can be tracked using git.


%description -l ru_RU.UTF-8
Простой консольный менеджер паролей, следующий философии Unix.
Пароли сохраняются внутри защищенных с использованием GnuPG
текстовых файлов с именами, соответствующими названиям
веб-сайтов или ресурсов. Файлы с паролями могут быть
организованы в произвольной иерархии каталогов, копироваться
с компьютера на компютер, и, в общем случае, обрабатываться
стандартными утилитами.

Поддерживается использование нескольких ключей GPG для
случая использования pass в совместной работе, разные
каталоги могут иметь разные наборы ключей GPG.
Все изменения паролей могут отслеживаться в репозитории Git.


%prep
%setup -q
%patch0 -p1

%patch1
%patch2

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
# This can't be run inside hasher
%ifdef __BTE
   rm -f tests/t0300-reencryption.sh
   rm -f tests/t0400-grep.sh
%endif
LC_ALL=C %make test

%install
%make_install DESTDIR=%buildroot FORCE_ALL=1 install

install -dp %buildroot%_sysconfdir/bash_completion.d/
mv -f -- %buildroot%_datadir/bash-completion/completions/pass %buildroot%_sysconfdir/bash_completion.d/pass

chmod 644 -- contrib/importers/*

install -dp %buildroot%vim_plugin_dir
mv -f -- contrib/vim/noplaintext.vim %buildroot%vim_plugin_dir/password-store.vim
rmdir -- contrib/vim/

%files
%doc README contrib
%doc --no-dereference COPYING

%_bindir/pass
%_man1dir/pass.*

%_sysconfdir/bash_completion.d/pass
%vim_plugin_dir/password-store.vim

%exclude %_datadir/fish*
%exclude %_datadir/zsh*

%changelog
* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.6.5-alt1
- Initial build for ALT Linux Sisyphus
