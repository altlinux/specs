Epoch: 0
Group: Graphics
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           batik
Version:        1.8
Release:        alt3_6jpp8
Summary:        Scalable Vector Graphics for Java
License:        ASL 2.0 and W3C
URL:            http://xml.apache.org/batik/
Source0:        http://apache.crihan.fr/dist/xmlgraphics/batik/source/batik-src-%{version}.zip
Source1:        %{name}.squiggle.script
Source2:        %{name}.svgpp.script
Source3:        %{name}.ttf2svg.script
Source4:        %{name}.rasterizer.script
Source5:        %{name}.slideshow.script
Source6:        %{name}-squiggle.desktop
Source7:        %{name}-repack.sh

# These manifests with OSGi metadata are taken from the Eclipse Orbit
# project:  http://download.eclipse.org/tools/orbit/downloads/drops/R20110523182458/
#
# for f in `ls *.jar`; do unzip -d `basename $f .jar | sed s/_.*//` $f; done
# for f in `find -name MANIFEST.MF`; do mv $f $(echo $f | sed "s|./org.apache.||" | sed "s|/META-INF/|-|" | sed "s/\./-/g" | sed "s|MANIFEST-MF|MANIFEST.MF|"); done
# Then manually remove all lines containing MD5sums/crypto hashes.
# tar czf batik-1.6-orbit-manifests.tar.gz *.MF
#
Source8:        %{name}-1.7-orbit-manifests.tar.gz

Source9:        %{name}-security.policy


Patch0:         %{name}-manifests.patch
# remove dependency on bundled rhino from pom
Patch2:         %{name}-script-remove-js.patch

# make sure we fail build if javadocs fail (run OOM)
# also make maxmem a bit higher. we seem to need more...
# https://issues.apache.org/jira/browse/BATIK-1065
Patch3:         %{name}-javadoc-task-failonerror-and-oom.patch

Patch4:         %{name}-disable-doclint.patch

Patch5:         %{name}-fix-codec-lookup.patch

BuildArch:      noarch

BuildRequires:  java-devel >= 1.6.0
BuildRequires:  maven-local >= 1.5
BuildRequires:  ant
BuildRequires: subversion subversion-server-common
BuildRequires:  zip

BuildRequires:  rhino >= 1.5
BuildRequires:  jpackage-utils >= 1.5
BuildRequires:  xerces-j2
BuildRequires:  xalan-j2
BuildRequires:  xml-commons-apis >= 1.3.04
BuildRequires:  xmlgraphics-commons

BuildRequires:  java-javadoc >= 1:1.6.0

#full support for tiff
Requires:       jai-imageio-core
Requires:       rhino >= 1.5
Requires:       xalan-j2
Requires:       xml-commons-apis >= 1.3.04
Requires:       %{name}-css = %{version}
Source44: import.info
#19119
Provides: xmlgraphics-batik = 0:%version-%release
Obsoletes: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version


%description
Batik is a Java(tm) technology based toolkit for applications that want
to use images in the Scalable Vector Graphics (SVG) format for various
purposes, such as viewing, generation or manipulation.

%package css
Group: Graphics
Summary:        Batik CSS engine
Obsoletes:      %{name} < 1.8-0.17.svn1230816
#32067
Conflicts: batik < 0:1.8-alt1_1

%description css
CSS component of the Apache Batik SVG manipulation and rendering library.

%package        squiggle
Summary:        Batik SVG browser
Group:          Graphics
Requires:       %{name} = %{version}
Requires:       xerces-j2 >= 2.3
#19119
Provides: xmlgraphics-batik-squiggle = 0:%version-%release
Obsoletes: xmlgraphics-batik-squiggle < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    squiggle
The Squiggle SVG Browser lets you view SVG file, zoom, pan and rotate
in the content and select text items in the image and much more.

%package        svgpp
Summary:        Batik SVG pretty printer
Group:          Graphics
Requires:       %{name} = %{version}
Requires:       xerces-j2 >= 2.3
#19119
Provides: xmlgraphics-batik-svgpp = 0:%version-%release
Obsoletes: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    svgpp
The SVG Pretty Printer lets developers "pretty-up" their SVG files and
get their tabulations and other cosmetic parameters in order. It can
also be used to modify the DOCTYPE declaration on SVG files.

%package        ttf2svg
Summary:        Batik SVG font converter
Group:          Graphics
Requires:       %{name} = %{version}
#19119
Provides: xmlgraphics-batik-ttf2svg = 0:%version-%release
Obsoletes: xmlgraphics-batik-ttf2svg < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    ttf2svg
The SVG Font Converter lets developers convert character ranges from
the True Type Font format to the SVG Font format to embed in SVG
documents. This allows SVG document to be fully self-contained be
rendered exactly the same on all systems.

%package        rasterizer
Summary:        Batik SVG rasterizer
Group:          Graphics
Requires:       %{name} = %{version}
Requires:       xerces-j2 >= 2.3
#19119
Provides: xmlgraphics-batik-rasterizer = 0:%version-%release
Obsoletes: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    rasterizer
The SVG Rasterizer is a utility that can convert SVG files to a raster
format. The tool can convert individual files or sets of files, making
it easy to convert entire directories of SVG files. The supported
formats are JPEG, PNG, and TIFF, however the design allows new formats
to be added easily.

%package        slideshow
Summary:        Batik SVG slideshow
Group:          Graphics
Requires:       %{name} = %{version}
Requires:       xerces-j2 >= 2.3
#19119
Provides: xmlgraphics-batik-slideshow = 0:%version-%release
Obsoletes: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    slideshow
Batik SVG slideshow.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        demo
Group: Development/Java
Summary:        Demo for %{name}
Requires:       %{name} = %{version}

%description    demo
Demonstrations and samples for %{name}.


%prep
%setup -q -n %{name}-%{version}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

#%patch0 -p1
rm -f `find -name readOnly.png`
rm -f `find -name properties`
mkdir orbit
pushd orbit
tar xzf %{SOURCE8}
popd

cp -p %{SOURCE9} resources/org/apache/batik/apps/rasterizer/resources/rasterizer.policy.ref
cp -p %{SOURCE9} resources/org/apache/batik/apps/svgbrowser/resources/svgbrowser.policy.ref

# create poms from templates
for module in anim awt-util bridge codec css dom ext extension gui-util \
              gvt parser script svg-dom svggen swing transcoder util xml \
              rasterizer slideshow squiggle svgpp ttf2svg; do
      sed "s:@version@:%{version}:g" sources/%{name}-$module.pom.template \
         > %{name}-$module.pom
done
#%patch2

#%patch3
%patch4
%patch5 -p1

rm -fr sources/org/apache/batik/ext/awt/image/codec/tiff

%build

export ANT_OPTS="-Xmx512m"
# due to javadoc x86_64 out of memory
subst 's,maxmemory="128m",maxmemory="512m",' build.xml
export CLASSPATH=$(build-classpath xml-commons-apis xml-commons-apis-ext xmlgraphics-commons js rhino xalan-j2 xalan-j2-serializer xerces-j2)
ant all-jar jars\
        -Ddebug=on \
        -Dsun-codecs.present=false \
        -Dsun-codecs.disabled=true \
        svg-pp-jar \
        svg-slideshow-jar \
        squiggle-jar \
        rasterizer-jar \
        ttf2svg-jar

ant javadoc


%install
# inject OSGi manifests
mkdir -p META-INF
cp -p orbit/batik-bridge-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-bridge-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-css-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-css-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-dom-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-dom-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-dom-svg-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-svg-dom-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-ext-awt-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-awt-util-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-extension-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-extension-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-parser-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-parser-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-svggen-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-svggen-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-swing-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-swing-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-transcoder-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-transcoder-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-util-gui-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-gui-util-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-util-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-util-%{version}.jar META-INF/MANIFEST.MF
cp -p orbit/batik-xml-MANIFEST.MF META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}-%{version}/lib/batik-xml-%{version}.jar META-INF/MANIFEST.MF


# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
pushd %{name}-%{version}/lib
for jarname in $(find batik-*.jar); do
    cp -p ${jarname} $RPM_BUILD_ROOT%{_javadir}/%{name}/${jarname//-1.8/}
done

rm -fr $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-all.jar
cp -p %{name}-all-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-all.jar

popd

pushd %{name}-%{version}
for module in rasterizer slideshow squiggle svgpp ttf2svg; do
	cp -p batik-$module-%{version}.jar  $RPM_BUILD_ROOT%{_javadir}/batik-$module.jar
done
popd

# poms and depmaps for subpackages are different (no batik subdir)
install -d -m 755 $RPM_BUILD_ROOT/%{_mavenpomdir}
for module in rasterizer slideshow squiggle svgpp ttf2svg; do
      install -pm 644 %{name}-$module.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}-$module.pom
      %add_maven_depmap JPP-%{name}-$module.pom %{name}-$module.jar -a "%{name}:%{name}-$module" -f $module
done

# css pom files and maven depmaps
for module in css gui-util util; do
      install -pm 644 %{name}-$module.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-%{name}-$module.pom
      %add_maven_depmap JPP.%{name}-%{name}-$module.pom %{name}/%{name}-$module.jar -a "%{name}:%{name}-$module" -f css
done

# main pom files and maven depmaps
for module in anim awt-util bridge codec dom ext extension \
              gvt parser script svg-dom svggen swing transcoder xml; do

      install -pm 644 %{name}-$module.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-%{name}-$module.pom
      %add_maven_depmap JPP.%{name}-%{name}-$module.pom %{name}/%{name}-$module.jar -a "%{name}:%{name}-$module"
done

# scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/squiggle
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/svgpp
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/ttf2svg
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/rasterizer
cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/slideshow

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr %{name}-%{version}/docs/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr contrib resources samples test-resources test-sources \
  $RPM_BUILD_ROOT%{_datadir}/%{name}

#Fix perms
chmod +x $RPM_BUILD_ROOT%{_datadir}/%{name}/contrib/rasterizertask/build.sh
chmod +x $RPM_BUILD_ROOT%{_datadir}/%{name}/contrib/charts/convert.sh

mkdir -p $RPM_BUILD_ROOT`dirname /etc/rasterizer.conf`
touch $RPM_BUILD_ROOT/etc/rasterizer.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/slideshow.conf`
touch $RPM_BUILD_ROOT/etc/slideshow.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/squiggle.conf`
touch $RPM_BUILD_ROOT/etc/squiggle.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/svgpp.conf`
touch $RPM_BUILD_ROOT/etc/svgpp.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/ttf2svg.conf`
touch $RPM_BUILD_ROOT/etc/ttf2svg.conf

mkdir -p $RPM_BUILD_ROOT%_javadir/xmlgraphics-batik
pushd $RPM_BUILD_ROOT%_javadir/xmlgraphics-batik
  ln -s ../batik/batik-anim.jar batik-anim.jar
  ln -s ../batik/batik-awt-util.jar batik-awt-util.jar
  ln -s ../batik/batik-bridge.jar batik-bridge.jar
  ln -s ../batik/batik-codec.jar batik-codec.jar
  ln -s ../batik/batik-css.jar batik-css.jar
  ln -s ../batik/batik-dom.jar batik-dom.jar
  ln -s ../batik/batik-ext.jar batik-ext.jar
  ln -s ../batik/batik-extension.jar batik-extension.jar
  ln -s ../batik/batik-gui-util.jar batik-gui-util.jar
  ln -s ../batik/batik-gvt.jar batik-gvt.jar
  ln -s ../batik/batik-parser.jar batik-parser.jar
  ln -s ../batik/batik-script.jar batik-script.jar
  ln -s ../batik/batik-svg-dom.jar batik-svg-dom.jar
  ln -s ../batik/batik-svggen.jar batik-svggen.jar
  ln -s ../batik/batik-swing.jar batik-swing.jar
  ln -s ../batik/batik-transcoder.jar batik-transcoder.jar
  ln -s ../batik/batik-util.jar batik-util.jar
  ln -s ../batik/batik-xml.jar batik-xml.jar
  ln -s ../batik-rasterizer.jar rasterizer.jar
popd


%files -f .mfiles
%doc LICENSE NOTICE
%doc KEYS MAINTAIN README
%{_javadir}/%{name}-all.jar
%dir %{_javadir}/batik
%_javadir/xmlgraphics-batik/batik-anim.jar
%_javadir/xmlgraphics-batik/batik-awt-util.jar
%_javadir/xmlgraphics-batik/batik-bridge.jar
%_javadir/xmlgraphics-batik/batik-codec.jar
%_javadir/xmlgraphics-batik/batik-css.jar
%_javadir/xmlgraphics-batik/batik-dom.jar
%_javadir/xmlgraphics-batik/batik-ext.jar
%_javadir/xmlgraphics-batik/batik-extension.jar
%_javadir/xmlgraphics-batik/batik-gui-util.jar
%_javadir/xmlgraphics-batik/batik-gvt.jar
%_javadir/xmlgraphics-batik/batik-parser.jar
%_javadir/xmlgraphics-batik/batik-script.jar
%_javadir/xmlgraphics-batik/batik-svg-dom.jar
%_javadir/xmlgraphics-batik/batik-svggen.jar
%_javadir/xmlgraphics-batik/batik-swing.jar
%_javadir/xmlgraphics-batik/batik-transcoder.jar
%_javadir/xmlgraphics-batik/batik-util.jar
%_javadir/xmlgraphics-batik/batik-xml.jar

%files css -f .mfiles-css

%files squiggle -f .mfiles-squiggle
%attr(0755,root,root) %{_bindir}/squiggle
%config(noreplace,missingok) /etc/squiggle.conf

%files svgpp -f .mfiles-svgpp
%attr(0755,root,root) %{_bindir}/svgpp
%config(noreplace,missingok) /etc/svgpp.conf

%files ttf2svg -f .mfiles-ttf2svg
%attr(0755,root,root) %{_bindir}/ttf2svg
%config(noreplace,missingok) /etc/ttf2svg.conf

%files rasterizer -f .mfiles-rasterizer
%attr(0755,root,root) %{_bindir}/rasterizer
%config(noreplace,missingok) /etc/rasterizer.conf
%_javadir/xmlgraphics-batik/rasterizer.jar

%files slideshow -f .mfiles-slideshow
%attr(0755,root,root) %{_bindir}/slideshow
%config(noreplace,missingok) /etc/slideshow.conf

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}


%changelog
* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt3_6jpp8
-dropped deprecated upgrade hack (closes: #32819)

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt2_6jpp8
- new fc release

* Thu May 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt2_2jpp8
- added conflicts (closes: #32067)

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_0.10.svn1230816jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_0.7.svn1230816jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_0.5.svn1230816jpp7
- fc update

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_0.4.svn1230816jpp7
- new version

* Fri Sep 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt7_14jpp6
- added compat symlinks

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt6_14jpp6
- updated OSGi manifest

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt6_7jpp6
- added OSGi provides

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt6_5jpp5
- proper fix of #19119. Thanks to mithraen@ for report.

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt5_5jpp5
- fixed #19119

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt4_5jpp5
- added batik dir symlink

* Thu Sep 11 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_5jpp5
- fixed unmets

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_5jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_5jpp5
- converted from JPackage by jppimport script

