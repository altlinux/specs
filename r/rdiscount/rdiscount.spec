Name:    rdiscount
Version: 2.2.0.1
Release: alt1.1

Summary: Discount (For Ruby) Implementation of John Gruber's Markdown
License: BSD-3-Clause
Group:   Development/Ruby
Url:     https://github.com/davidfstr/rdiscount

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%description
Discount is an implementation of John Gruber's Markdown markup language
in C. It implements all of the language described in the markdown syntax
document and passes the Markdown 1.0 test suite.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

mkdir -p %buildroot%_man7dir
mv %buildroot%_mandir/*.7 %buildroot%_man7dir
mkdir -p %buildroot%_man1dir
mv %buildroot%_mandir/*.1 %buildroot%_man1dir
rm -f %buildroot%_mandir/*.*

%check
%ruby_test_unit -Ilib:ext:test test/*.rb

%files
%doc README*
%_bindir/%name
%ruby_sitelibdir/*
%_man1dir/*.1*
%_man7dir/*.7*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Jun 09 2018 Alexey Shabalin <shaba@altlinux.ru> 2.2.0.1-alt1.1
- NMU: rebuild for aarch64

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0.1-alt1
- Initial build for Sisyphus
