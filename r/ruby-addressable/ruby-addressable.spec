Name:    ruby-addressable
Version: 2.5.2
Release: alt2

Summary: Addressable is a replacement for the URI implementation that is part of Ruby's standard library
Summary(ru_RU.UTF-8): "Адресуемый" есть заменою воплощения URI, который является частью стандартной библиотеки рубина
Group:   Development/Ruby
License: MIT/Ruby
URL:     http://addressable.rubyforge.org/
# VCS:   https://github.com/sporkmonger/addressable.git

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

Source: %name-%version.tar

%description
Addressable is a replacement for the URI implementation that is part of
Ruby's standard library. It more closely conforms to RFC 3986, RFC 3987,
and RFC 6570 (level 4), providing support for IRIs and URI templates.

%description -l ru_RU.UTF-8
"Адресуемый" есть замена воплощения URI, который является частью стандартной
библиотеки рубина. Бн более точно удовлетворяет стандартам RFC 3986, RFC 3987,
и RFC 6570 (уровня 4), поддержиивая IRI и URI шаблоны.

%package doc
Summary:   Documentation for %name
Group:     Development/Documentation
Requires:  %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %{name}.

%description -l ru_RU.UTF-8 doc
Документация для %{name}.

%prep
%setup -n %name-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%check
#rspec

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
mkdir -p %buildroot%_datadir/%name
mv %buildroot%_datadir/unicode.data %buildroot%_datadir/%name/unicode.data

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*
%_datadir/%name

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Dec 24 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt2
- Fixed packing procedure of the "unicode.data" file
- Added russian translations to spec.

* Sun Aug 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.2-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Aug 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.2-alt1
- New version

* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Sun Jun 05 2016 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- Initial build for ALT Linux
