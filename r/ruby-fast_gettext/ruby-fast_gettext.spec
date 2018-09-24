%define  pkgname fast_gettext
 
Name: 	 ruby-%pkgname
Version: 1.7.0
Release: alt1
 
Summary: GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7 vs 34) and threadsafe!
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/grosser/fast_gettext
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby

%description
GetText but 3.5 x faster, 560 x less memory, simple, clean namespace (7
vs 34) and threadsafe!

It supports multiple backends (.mo, .po, .yml files,
Database(ActiveRecord + any other), Chain, Loggers) and can easily be
extended.

%description -l ru_RU.UTF8
Текущая GetText в 3,5 раза быстрее 560 раз потребляющая память, простая и ясная
в употреблении (7 против 34 пространств имён) и потокобезопасная.

Поддерживает различные конечные точки (.mo, .po, .yml файлы, базы данных
ActiveRecord и другие, цепи и логеры), а также есть легко расширяемым.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%description doc -l ru_RU.UTF8
Файлы сведений для %name

%prep
%setup -n %pkgname-%version
%update_setup_rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install

%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc Readme*
%ruby_sitelibdir/*
%rubygem_specdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- Bump to 1.7.0.

* Thu Sep 20 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt3.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt3
- Fix package as gem.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- Rebuild with Ruby 2.4.2

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build in Sisyphus
