import streamlit as st
import urllib.parse

# --- CONFIGURACIÓN DE PÁGINA Y ESTILO ---
st.set_page_config(
    page_title="Elefante Gris | Asesoría Artística",
    page_icon="🐘",
    layout="centered"
)

# --- CSS PERSONALIZADO (Para darle el toque "Cine/Editorial") ---
st.markdown("""
    <style>
    /* Tipografía elegante */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #2C2C2C;
        font-weight: 300; /* Letra fina y elegante */
    }
    .main-text {
        color: #4F4F4F;
        font-size: 18px;
        line-height: 1.6;
    }
    /* Estilo para los botones de pestañas */
    div[data-testid="stTabs"] button {
        font-size: 18px;
    }
    /* Eliminar borde superior rojo de Streamlit */
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA (LOGO Y NOMBRE) ---
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("# 🐘") # Aquí iría tu logo real si tuvieras imagen
with col2:
    st.title("ELEFANTE GRIS")
    st.caption("ASESORAMIENTO ARTÍSTICO PARA PRODUCTORAS DE CINE")

st.markdown("---")

# --- NAVEGACIÓN POR PESTAÑAS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Inicio", "Conócenos", "Saber Más", "Servicios", "Contacto"])

# --- PESTAÑA 1: INICIO ---
with tab1:
    st.header("La estructura detrás de la visión.")
    st.markdown("""
    <div class='main-text'>
    En <b>Elefante Gris</b>, entendemos que una gran película no solo nace de una idea, 
    sino de la arquitectura que la sostiene.<br><br>
    Aportamos la solidez necesaria para que el caos creativo se transforme en obra maestra.
    Nos especializamos en blindar artísticamente tus proyectos desde el guion hasta el set.
    </div>
    """, unsafe_allow_html=True)
    
    # Imagen de portada (puedes poner una url real de unsplash o tuya)
    st.image("https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=2059&auto=format&fit=crop", 
             caption="Cine es estructura y emoción.", use_container_width=True)

# --- PESTAÑA 2: CONÓCENOS ---
with tab2:
    st.header("Quiénes Somos")
    st.write("Somos un colectivo de directores, guionistas y productores ejecutivos dedicados a elevar el estándar narrativo.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("🎯 **Nuestra Misión**\n\nDetectar las grietas narrativas y logísticas antes de que se conviertan en problemas de rodaje.")
    with col_b:
        st.success("👁️ **Nuestra Visión**\n\nSer el 'partner' invisible pero indispensable de las grandes productoras independientes.")

# --- PESTAÑA 3: SABER MÁS (Metodología) ---
with tab3:
    st.header("Nuestra Metodología")
    st.write("No somos externos que opinan, somos aliados que construyen.")
    
    st.markdown("""
    1.  **Inmersión:** Leemos, visualizamos y entendemos el tono único de tu proyecto.
    2.  **Diagnóstico:** Entregamos un reporte de 'Salud Artística' del proyecto.
    3.  **Ejecución:** Nos integramos con tus cabezas de equipo para alinear la visión.
    """)

# --- PESTAÑA 4: SERVICIOS (Con desplegables) ---
with tab4:
    st.header("Nuestros Servicios")
    st.write("Haz clic en cada área para ver el detalle de nuestra intervención.")

    # SERVICIO 1
    with st.expander("📝 ANÁLISIS Y DOCTORING DE GUIONES"):
        st.markdown("""
        * **Análisis estructural:** Ritmo, detonantes y arcos de personajes.
        * **Diálogos:** Pulido de subtexto y naturalidad.
        * **Viabilidad:** Reporte de 'Escenas de Riesgo' (presupuesto vs. narrativa).
        """)

    # SERVICIO 2
    with st.expander("🎨 GESTIÓN DE EQUIPOS CREATIVOS"):
        st.markdown("""
        * Selección de Jefes de Área (Arte, Fotografía, Vestuario) alineados a la estética.
        * Mediación entre Director y Productor.
        * Creación de 'Biblias de Estilo' visual.
        """)

    # SERVICIO 3
    with st.expander("🎬 SUPERVISIÓN DE PRODUCCIÓN GENERAL"):
        st.markdown("""
        * Presencia en set para garantizar la coherencia artística.
        * Supervisión de casting.
        * Control de calidad en el montaje final y colorización.
        """)

# --- PESTAÑA 5: CONTACTO ---
with tab5:
    st.header("Hablemos de tu próximo proyecto")
    
    st.write("¿Tienes un guion en mano o una producción en curso? Estamos listos para escuchar.")
    
    # --- BOTÓN DE WHATSAPP ---
    NUMERO_WHATSAPP = "5493510000000" # <--- CAMBIA ESTO POR TU NÚMERO
    mensaje_wpp = "Hola Elefante Gris, me gustaría agendar una asesoría para mi productora."
    link_wpp = f"https://wa.me/{NUMERO_WHATSAPP}?text={urllib.parse.quote(mensaje_wpp)}"
    
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="{link_wpp}" target="_blank" style="
            background-color: #2C2C2C; 
            color: white; 
            padding: 15px 30px; 
            text-decoration: none; 
            border-radius: 5px; 
            font-size: 18px; 
            font-weight: bold;
            letter-spacing: 1px;">
            HABLEMOS POR WHATSAPP 🐘
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.info("✉️ O escríbenos a: contacto@elefantegris.com")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("© 2025 Elefante Gris Consultora. Todos los derechos reservados.")
