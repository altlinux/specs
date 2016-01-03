# debuginfo extraction currently fails with
# "Failed to write file: invalid section alignment"
%global __find_debuginfo_files %nil

%global _unpackaged_files_terminate_build 1

%global gopath          %_datadir/gocode
%global goroot          %_datadir/gocode

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %goroot %_bindir
%brp_strip_none %_bindir/*

%global provider        github
%global provider_tld    com
%global project         rekby
%global repo            fsextender
# https://github.com/rekby/fsextender
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name: fsextender
Version: 0.1.4
Release: alt1
Summary: Extend filesystems with underliing layers: partitions, lvm on mbr and gpt disks
License: MIT
Url: https://github.com/rekby/fsextender
Group: System/Configuration/Hardware

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: golang golang-github-rekby-gpt-devel golang-github-rekby-mbr-devel  golang-github-rekby-pflag-devel

%description
Extend filesystem to max size with underliing layers. It can extend:
ext3, ext4, xfs, LVM Logical volume, LVM Physical volume, LVM Volume
Group (with new or free pv) , partitions in MSDOS and GPT partition
tables. It can create new partitions and LVM Physical volumes on disk
with MSDOS and GPT partition tables.

%package devel
Group: Development/Other
Requires: golang
Summary: %{summary}
# Provides:      golang(%%{import_path}/common/util) = %%{version}-%%{release}

%description devel
This is the source libraries for fsextender.

%prep
%setup

%build
mkdir -p src/github.com/rekby

ln -s ../../../  src/github.com/rekby/fsextender
export GOPATH=$(pwd):$(pwd)/vendor:%{gopath}

mkdir bin
binaries=(fsextender)
for bin in "${binaries[@]}"; do
    go build -o bin/${bin} ${bin}/main.go
done

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/* %{buildroot}%{_bindir}

install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
sort -u -o devel.file-list devel.file-list

%files
%doc README.md usage.txt
%_bindir/*

%files devel
%{gopath}/src/%{import_path}

%changelog
* Sun Jan  3 2016 Terechkov Evgenii <evg@altlinux.org> 0.1.4-alt1
- Initial build for ALT Linux Sisyphus
