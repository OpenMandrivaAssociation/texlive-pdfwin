Name:		texlive-pdfwin
Version:	54074
Release:	1
Summary:	TeXLive pdfwin package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfwin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfwin.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive pdfwin package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfwin/pdfwin.cfg
%{_texmfdistdir}/tex/latex/pdfwin/pdfwin.sty
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucResampling.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem1.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem2.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem3.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem4.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem5.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem6.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/Bucuresti2003.tex
%doc %{_texmfdistdir}/doc/latex/pdfwin/JWGU-Logo.png
%doc %{_texmfdistdir}/doc/latex/pdfwin/Thumbs.db
%doc %{_texmfdistdir}/doc/latex/pdfwin/marble.png
%doc %{_texmfdistdir}/doc/latex/pdfwin/normprot.tex
%doc %{_texmfdistdir}/doc/latex/pdfwin/shortvec.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
