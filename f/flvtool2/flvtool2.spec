Name: flvtool2
Version: 1.0.6
Release: alt3.2

Summary: FLVTool2 is a manipulation tool for Macromedia Flash Video files (FLV)
Summary(ru_RU.UTF8): FLVTool2 утилита для манипуляций с Macromedia Flash Video files (FLV)
License: BSD 
Group: Development/Ruby
Url: https://rubyforge.org/projects/flvtool2
BuildArch: noarch

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

BuildRequires: rpm-build-ruby ruby-tool-setup

%description
FLVTool2 is a manipulation tool for Macromedia Flash Video files (FLV).
It can calculate a lot of meta data, insert an onMetaData tag, cut FLV
files, add cue points (onCuePoint), show the FLV structure and print
meta data information in XML or YAML.

%description -l ru_RU.UTF8
FLVTool2 утилита для манипуляций с Macromedia Flash Video files (FLV).
Она может высчитывать множество метаданных, вставлять onMetaData теги,
обрезать FLV файлы, добавлять точки маркеры, показывать структуру
FLV и выводить информацию о метаданных в XML или YAML.

%prep
%setup -q
%update_setup_rb
find  -name '._*' -print0 |xargs -r0 rm -rf --

%build
%ruby_config
%ruby_build

%install
%ruby_install
%find_lang %name

%files -f %name.lang
%doc CHANGELOG LICENSE README
%_bindir/*
%ruby_sitelibdir/*


%changelog
* Tue Sep 15 2009 Alexey Morsov <swi@altlinux.ru> 1.0.6-alt3.2
- rebuild with 1.9 (patch from raorn)

* Mon Jul 20 2009 Alexey Morsov <swi@altlinux.ru> 1.0.6-alt3.1
- rebuild as noarch

* Thu Jul 16 2009 Alexey Morsov <swi@altlinux.ru> 1.0.6-alt3
- rebuild

* Wed Jul 15 2009 Alexey Morsov <swi@altlinux.ru> 1.0.6-alt2
- rebuild with ruby 1.9

* Wed Mar 21 2007 Alexey Morsov <swi@altlinux.ru> 1.0.6-alt1
- first build for Sisyphus

