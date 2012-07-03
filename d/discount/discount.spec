
Name: discount
Version: 1.6.5
Release: alt1

Summary: A implementation of John Gruber's Markdown markup language.
License: BSD
Group: Text tools
Url: http://www.pell.portland.or.us/~orc/Code/discount/
Packager: Kirill A. Shutemov <kas@altlinux.org>

Source: %name-%version.tar

%description
DISCOUNT is a implementation of John Gruber's Markdown markup language.

%prep
%setup -q

%build
# non-GNU configure
./configure.sh \
	--prefix=%_prefix \
	--enable-all-features
%make

%check
%make test

%install
mkdir -p %buildroot/%_bindir
%make DESTDIR=%buildroot install.everything

%files
%_bindir/*
%_man1dir/*
%_man3dir/*
%_man7dir/*

%changelog
* Wed Jun 16 2010 Kirill A. Shutemov <kas@altlinux.org> 1.6.5-alt1
- First build for ALT Linux Sisyphus

