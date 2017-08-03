%global _unpacked_files_terminate_build 1

Name: 	 asciidoctor
Version: 1.5.6.1 
Release: alt1

Summary: A fast text processor and publishing toolchain for converting AsciiDoc content to different formats
License: MIT
Group:   Development/Ruby
Url:     https://github.com/asciidoctor/asciidoctor

Packager: Gordeev Mikhail <obirvalger@altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar
Patch1:  asciidoctor-1.5.6.1-alt-fix-DATA_PATH.patch

%filter_from_requires \!^ruby(asciidoctor/js)$!d

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Asciidoctor is a fast text processor and publishing toolchain for converting
AsciiDoc content to HTML5, DocBook 5 (or 4.5) and other formats.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version
%update_setup_rb
%patch1 -p1

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

mkdir -p %buildroot%_datadir/%name
mv %buildroot%_datadir{,/%name}/stylesheets

mkdir -p %buildroot%_man1dir
mv %buildroot{%_mandir,%_man1dir}/%name.1
rm %buildroot%_mandir/%name.adoc
rm %buildroot%_datadir/locale/attributes.adoc

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%doc data/locale/attributes.adoc man/%name.adoc
%_bindir/%name
%_bindir/%name-safe
%_man1dir/%name.1.xz
%_datadir/%name/
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Aug 03 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.6.1-alt1
- Initial build for Sisyphus
