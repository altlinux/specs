Name:     pdfgrep
Version:  2.1.2
Release:  alt1

Summary:  pdfgrep is a tool to search text in PDF files. It works similarly to grep.
License:  GPLv2
Group:    File tools
Url:      https://pdfgrep.org
# repacked https://pdfgrep.org/download/%name-%version.tar.gz

Source:   %name-%version.tar

BuildRequires: make gcc gcc-c++
BuildRequires: libpoppler-cpp-devel libgcrypt-devel libpcre-devel

%description
%summary

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc *.md
%_bindir/*
%_man1dir/*
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name

%changelog
* Thu Aug 18 2022 Nikolay Burykin <bne@altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus
