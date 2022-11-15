%define _unpackaged_files_terminate_build 1

Name: plastex
Version: 2.1
Release: alt1.1

Summary: Plastex is a Python-based LaTeX document processing framework
Summary(ru_RU.UTF-8): Plastex - средство для обработки документов LaTex, написанное на Python

License: distributable
Group: Publishing
Url: http://plastex.sourceforge.net
BuildArch: noarch

Source0: %name-%version.tgz
Source1: %name.pdf

BuildRequires(pre): rpm-build-python3

Requires: dvipng
Requires: ghostscript
Requires: texlive-latex-base

%add_python3_self_prov_path %buildroot%python3_sitelibdir/plasTeX/Base/LaTeX/

%description
plasTeX is a LaTeX document processing framework written entirely in Python. 
It currently comes bundled with an XHTML renderer (including multiple themes), 
as well as a way to simply dump the document to a generic form of XML. Other 
renderers can be added as well and are planned for future releases.

%description -l ru_RU.UTF-8
Plastex - средство для обработки документов LaTex, написанное на Python. 
В настоящее время оно поставляется со средством рендеринга XHTML (включая
множество тем), а также умеет конвертировать документ в обычный XML. 
Другие средства рендеринга будут добавлены в будущие релизы.

%prep
%setup -n %name

%build
%python3_build

%install
%python3_install

mkdir -p %buildroot/%_defaultdocdir/%name-%version/licenses

cp licenses/* %buildroot/%_defaultdocdir/%name-%version/licenses/
cp %{SOURCE1} %buildroot/%_defaultdocdir/%name-%version/

%files
%doc LICENSE README.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.1-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Dec 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1-alt1
- Version updated to 2.1
- porting on python3

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1.1.qa1
- NMU: applied repocop patch

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt1.1
- Rebuild with Python-2.7

* Mon Nov 1 2010 Anton Chernyshov <ach@altlinux.org> 0.9.2-alt1
- create spec file
- add documentation to package


