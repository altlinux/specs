Name:           nfcollect
Version:        0.2
Release:        alt1
Summary:        Collect Netfilter NFLOG log entries and commit them to stable storage
Source:         %name-%version.tar.gz
Patch0:         0001-Remove-CLANG-only-build.patch
Patch1:         0002-Provide-max_entries-option.patch
Patch2:         0003-incorrect-size_t-printf.patch
URL:            https://github.com/yunchih/nfcollect
Group:          Networking/Other
License:        MIT

# Automatically added by buildreq on Tue Dec 10 2024
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error perl python3-base sh5
BuildRequires: libnetfilter_log-devel libsqlite3-devel libzstd-devel

%description
Collect packets from Netfilter netlink kernel interface. Packets are
aggregated onto a memory region (we call it a trunk), until the trunk is
full. A full trunk will be committed to disk by configurable means
(currently zstd compression and no compression is implemented). Trunks
will be stored in a specific directory, which will be scanned by
nfextract to extract all trunks.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*

%changelog
* Tue Dec 10 2024 Fr. Br. George <george@altlinux.ru> 0.2-alt1
- Initial build for ALT
