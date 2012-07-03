%define origname chunkfs

Name: fuse-%origname
Version: 0.4
Release: alt1.1
License: GPL2
Group: System/Kernel and hardware
Url: http://chunkfs.florz.de/
Summary: FUSE-Filesystem to mount a file or block device as a chunks directory
Summary(ru_RU.UTF-8): Основанная на FUSE ФС для монтирования файла или блочного устройства в виде "кусочков"

Source: %origname-%version.tar

BuildRequires: libfuse-devel
BuildRequires: perl-podlators

%description
ChunkFS is a FUSE  based filesystem that allows you to mount an arbitrary file
or block device as a directory tree of files that each represent a chunk of
user-specified size of the mounted file.
ChunkFS was written for making space-efficient incremental backups of encrypted
filesystem images using rsync. Using the --link-dest option of rsync, you can
create incremental backups from the ChunkFS-mounted image where any chunk that
hasn't changed since the last backup will be a hard link to the corresponding
chunk from the previous backup.

%prep
%setup -q -n %origname-%version
subst 's|LDFLAGS|LDLIBS|' Makefile

%build
make
gunzip chunkfs.1.gz

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install {,un}chunkfs %buildroot%_bindir
install chunkfs.1 %buildroot%_man1dir
mkdir examples && cp -a writeoverlay.sh examples

%files
%doc examples
%_bindir/*
%_man1dir/*

%changelog
* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu May 21 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.4-alt1
- 1st release to ALTLinux
