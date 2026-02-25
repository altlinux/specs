%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict
%def_with check
%global lfsflags -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE

Name: rmlint
Version: 2.10.3
Release: alt1

Summary: Extremely fast tool to remove duplicates and other lint from your filesystem
Summary(ru_RU.UTF-8): Быстрый поиск дубликатов файлов и другого мусора в файловой системе

License: GPLv3+
Group: File tools
Url: https://rmlint.readthedocs.io/en/latest/tutorial.html
Vcs: https://github.com/sahib/rmlint.git

Source0: %name-%version.tar
Patch0: rmlint-2.10.3-alt1-pytest3.patch

BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: libblkid-devel
BuildRequires: libelf-devel
BuildRequires: libjson-glib-devel
BuildRequires: scons
BuildRequires: gettext

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: man-db
BuildRequires: pytest3
BuildRequires: python3-module-pyxattr
BuildRequires: python3-module-psutil
BuildRequires: ash
BuildRequires: git
%endif

BuildRequires: desktop-file-utils
BuildRequires: shared-mime-info

%description
rmlint finds space waste and other broken things on your filesystem and
offers to remove it. It detects:
- duplicate files and directories;
- nonstripped binaries;
- broken symbolic links;
- empty files and directories;
- files with broken user/group IDs;
and more.

%description -l ru_RU.UTF-8
rmlint находит "мусор" в файловой системе и предлагает его удалить.
Он умеет искать:
- дубликаты файлов и каталогов;
- несжатые бинарники с отладочной информацией;
- битые символические ссылки;
- пустые файлы и каталоги;
- файлы с некорректными UID/GID;
и многое другое.

%prep
%setup
%autopatch -p1

%build
scons config --without-gui \
    CPPFLAGS="%{lfsflags}" \
    CFLAGS="%{optflags} %{lfsflags}" \
    CCFLAGS="%{optflags} %{lfsflags}"

scons --without-gui %{?_smp_mflags} GDB=1 \
    CPPFLAGS="%{lfsflags}" \
    CFLAGS="%{optflags} %{lfsflags}" \
    CCFLAGS="%{optflags} %{lfsflags}"

%install
rm -rf %buildroot
scons --without-gui install GDB=1 \
    --prefix=%buildroot%prefix \
    --actual-prefix=%prefix \
    CPPFLAGS="%{lfsflags}" \
    CFLAGS="%{optflags} %{lfsflags}" \
    CCFLAGS="%{optflags} %{lfsflags}"

rm -f %buildroot%_datadir/glib-2.0/schemas/gschemas.compiled

%find_lang rmlint

%check
scons --without-gui test \
    CPPFLAGS="%{lfsflags}" \
    CFLAGS="%{optflags} %{lfsflags}" \
    CCFLAGS="%{optflags} %{lfsflags}"

%files -f rmlint.lang
%doc COPYING README.rst CHANGELOG.md

%_bindir/rmlint
%_mandir/man1/rmlint.1*

%changelog
* Thu Jan 29 2026 Georgij Tsarin <crystarm@altlinux.org> 2.10.3-alt1
- Initial build for ALT Sisyphus.
